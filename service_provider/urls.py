from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, FacilityViewSet, BookingRuleViewSet, HotelImageViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'booking-rules', BookingRuleViewSet)
router.register(r'hotel-images', HotelImageViewSet)  # Endpoint for hotel images

urlpatterns = [
    path('api/', include(router.urls)),
]
