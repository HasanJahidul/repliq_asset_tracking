from django.urls import path
from .views import *

urlpatterns = [
    path('add/',save_device_log, name='device_log.save_device_log'),
    path('get/',get_device_logs, name='device_log.get_device_logs')
]
