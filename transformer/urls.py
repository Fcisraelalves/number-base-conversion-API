from django.contrib import admin
from django.urls import path
from .views import decimal_to_binary
urlpatterns = [
    path('dec-to-bin/', decimal_to_binary),
]