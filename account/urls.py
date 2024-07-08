from django.urls import path
from .views import *

urlpatterns = [
    path('registerUser/',registerUser, name='registerUser'),
    path('registerVendor/', registerVendor, name="registerVendor")
]
