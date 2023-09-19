from django.urls import path

from . import views
from .views import *

app_name = "user"

urlpatterns = [
    path("login/", LoginPage, name="login"),
    path("logout/", LogOutPage, name="logout"),
    # path('register/',RegisterPage,name='register'),
    path("register/", views.Register.as_view(), name="register"),
    path(
        "confirm-email/<uidb64>/<token>",
        views.ConfirmRegisterView.as_view(),
        name="activate",
    ),
    path(
        "reset-password",
        views.ResetPasswordView.as_view(),
        name="reset-password",
    ),
    path(
        "confirm-reset-password/<uidb64>/<token>",
        views.ConfirmResetPasswordView.as_view(),
        name="reset-password-confirm",
    ),
]
