from django.urls import path
from .views import *

urlpatterns = [
    path('save/',save_employee, name='employee.save_employee'),
    path('get/',get_employees, name='employee.get_employees')
]
