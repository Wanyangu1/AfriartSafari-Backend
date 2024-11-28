from django.urls import path
from paypal_app import views

urlpatterns = [
    path('create_payment/', views.create_payment, name='create_payment'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
]
