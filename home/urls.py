from django.urls import path
from .import views

urlpatterns = [
    path("" , views.home , name='home'),
    path("singup/" , views.singup , name='singup'),
    path("login/" , views.user_login , name='login'),
    path("welcome/" , views.welcome , name='welcome')
]