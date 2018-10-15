from django.contrib import admin
from django.urls import path,include
from api.base.views.view_auth import login, register


urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('reset-password/', login, name="resetpassword"),

]


