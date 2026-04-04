from django.contrib import admin
from django.urls import path
from .views import decimal_to_binary, binary_to_decimal, decimal_to_octal, decimal_to_hex
urlpatterns = [
    path('dec-to-bin/', decimal_to_binary),
    path('dec-to-oct/', decimal_to_octal),
    path('dec-to-hex/', decimal_to_hex),

    path('bin-to-dec/', binary_to_decimal),
]

