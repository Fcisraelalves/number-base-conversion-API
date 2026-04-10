from django.contrib import admin
from django.urls import path
from .views import decimal_to_binary, binary_to_decimal, decimal_to_octal, decimal_to_hex, binary_to_gray, gray_to_binary, decimal_to_bcd, octal_to_decimal, hex_to_decimal
urlpatterns = [
    path('dec-to-bin/', decimal_to_binary),
    path('dec-to-oct/', decimal_to_octal),
    path('dec-to-hex/', decimal_to_hex),
    path('dec-to-bcd/', decimal_to_bcd),

    path('bin-to-gray/', binary_to_gray),
    path('gray-to-bin/', gray_to_binary),

    path('bin-to-dec/', binary_to_decimal),
    path('oct-to-dec/', octal_to_decimal),
    path('hex-to-dec/', hex_to_decimal),
    path('bcd-to-dec/', bcd_to_decimal),
]

