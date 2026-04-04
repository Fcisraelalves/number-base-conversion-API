from django.contrib import admin
from django.urls import path
from .views import decimal_to_binary, binary_to_decimal, decimal_to_octal
urlpatterns = [
    path('dec-to-bin/', decimal_to_binary),
    path('dec-to-oct/', decimal_to_octal),
    path('bin-to-dec/', binary_to_decimal),
]