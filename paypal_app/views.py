from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from rest_framework.decorators import api_view
from .models import Payment
from .serializers import PaymentSerializer
from booking.models import Booking  # Ensure this is the correct import for your Booking model
import paypalrestsdk
from booking_system.credentials import PAYPAL_SECRET, PAYPAL_CLIENT_ID

# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" in production
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_SECRET,
})

@api_view(["POST"])
def create_payment(request):
    """
    Handles the creation of a PayPal payment.
    Accepts `total_amount` and `booking_id` from the frontend.
    """
    if request.method == "POST":
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            total_amount = serializer.validated_data['total_amount']
            booking_id = serializer.validated_data['booking_id']

            try:
                # Retrieve the booking instance
                booking = Booking.objects.get(id=booking_id)
            except Booking.DoesNotExist:
                return JsonResponse({"error": "Invalid booking ID."}, status=400)

            # Create PayPal payment
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
                            "total": str(total_amount),
                            "currency": "USD",
                        },
                        "description": f"Payment for Booking ID {booking.id}",
                    }
                ],
            })

            if payment.create():
                approval_url = next(link.href for link in payment.links if link.rel == "approval_url")
                return JsonResponse({"approval_url": approval_url})
            else:
                return JsonResponse({"error": "Unable to create payment"}, status=400)
        else:
            return JsonResponse(serializer.errors, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)

def execute_payment(request):
    """
    Executes a PayPal payment after the user approves it.
    """
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    try:
        # Retrieve payment from PayPal
        payment = paypalrestsdk.Payment.find(payment_id)

        if payment.execute({"payer_id": payer_id}):
            # Extract the booking ID from the description
            description = payment.transactions[0].description
            booking_id = int(description.split(" ")[-1])  # Assumes "Payment for Booking ID {id}"

            # Save payment data to the database
            payment_record = Payment(
                payment_id=payment_id,
                payer_id=payer_id,
                amount=payment.transactions[0].amount.total,
                currency=payment.transactions[0].amount.currency,
                status=payment.state,
                description=payment.transactions[0].description,
                booking_id=booking_id  # Use the booking_id directly
            )
            payment_record.save()

            # Redirect to a success page
            return redirect('payment_successful', payment_id=payment_id)

    except paypalrestsdk.ResourceNotFound:
        return JsonResponse({"error": "Payment not found."}, status=404)

    return JsonResponse({"error": "Payment execution failed."}, status=400)

def payment_failed(request):
    """
    Handles a failed or canceled payment.
    """
    return JsonResponse({
        "status": "failed",
        "message": "Payment was canceled."
    })

def payment_successful(request, payment_id):
    """
    Displays the payment success page.
    """
    try:
        # Retrieve the payment from the database
        payment = Payment.objects.get(payment_id=payment_id)
        return render(request, 'payment_successful.html', {'payment': payment})
    except Payment.DoesNotExist:
        return JsonResponse({"error": "Payment not found."}, status=404)
