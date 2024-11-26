from django.urls import path, include
from .views import LogoutView, LoginView, RegisterView, UserProfileView
from .views import ChangePasswordView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="user-profile"), 
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
