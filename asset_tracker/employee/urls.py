from django.urls import path
from .views import *

urlpatterns = [
    path('save/',save_employee, name='employee.save_employee'),
]
