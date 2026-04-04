from django.contrib import admin
from django.urls import path
from .views import decimal_to_binary, binary_to_decimal
urlpatterns = [
    path('dec-to-bin/', decimal_to_binary),
    path('bin-to-dec/', binary_to_decimal),
]