from django.urls import path
from .views import *

urlpatterns = [
    path('add/',add_device, name='device.add_device'),
]
