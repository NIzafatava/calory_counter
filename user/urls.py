from django.urls import path
from .views import LoginPage,LogOutPage,RegisterPage



app_name = "user"

urlpatterns = [
    path('login/', LoginPage, name='login'),
    path('logout/',LogOutPage,name='logout'),
    path('register/',RegisterPage,name='register'),
]