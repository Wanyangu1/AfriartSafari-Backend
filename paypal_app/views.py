from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Payment
from .serializers import PaymentSerializer
import paypalrestsdk
from django.conf import settings
from django.urls import reverse
from rest_framework.decorators import api_view

from booking_system.credentials import PAYPAL_SECRET, PAYPAL_CLIENT_ID

# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" in production
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_SECRET,
})

# Create Payment
@api_view(["POST"])
def create_payment(request):
    print("Called")
    # Only handle POST request to process payment creation
    if request.method == "POST":
        print(request.POST)
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # Extract the dynamic amount from the request
            total_amount = serializer.validated_data['total_amount']
            # Create PayPal payment request with the dynamic total amount
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal",
                },
                "redirect_urls": {
                    "return_url": request.build_absolute_uri(reverse('execute_payment')),
                    "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
                },
                "transactions": [
                    {
                        "amount": {
                            "total": str(total_amount),  # Use dynamic amount here
                            "currency": "USD",
                        },
                        "description": "Payment for Product/Service",
                    }
                ],
            })

            if payment.create():
                # Find the approval URL for PayPal redirection
                approval_url = next(link.href for link in payment.links if link.rel == "approval_url")
                return JsonResponse({"approval_url": approval_url})
            else:
                return JsonResponse({"error": "Unable to create payment"}, status=400)
        else:
            return JsonResponse(serializer.errors, status=400)
    
    return JsonResponse({"error": "Invalid request method"}, status=400)

# Execute Payment (PayPal redirects here after successful payment)
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # Save the payment data to the database
        payment_record = Payment(
            payment_id=payment_id,
            payer_id=payer_id,
            amount=payment.transactions[0].amount.total,
            currency=payment.transactions[0].amount.currency,
            status=payment.state,
            description=payment.transactions[0].description
        )
        payment_record.save()

        # Redirect to the payment successful page
        return redirect('payment_successful', payment_id=payment_id)

    else:
        return JsonResponse({
            "status": "failed",
            "message": "Payment execution failed.",
            "paymentId": payment_id,
            "payerId": payer_id,
        }, status=400)

# Payment Failed (if user cancels payment)
def payment_failed(request):
    return JsonResponse({
        "status": "failed",
        "message": "Payment was canceled."
    })

# Payment Successful (Redirected after successful payment)
def payment_successful(request, payment_id):
    # Retrieve the payment from the database
    payment = Payment.objects.get(payment_id=payment_id)
    return render(request, 'payment_successful.html', {'payment': payment})

