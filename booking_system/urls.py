from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from paypal_app import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("booking_system.api.urls")),
    path("api/", include("booking.urls")),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
    path('payment_failed/', views.payment_failed, name='payment_failed'), 
    path('payment_successful/<str:payment_id>/', views.payment_successful, name='payment_successful'),
    path("", include("service_provider.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
