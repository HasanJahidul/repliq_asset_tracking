from django.urls import path
from .views import *

urlpatterns = [
    path('', hello_world, name='home'),
    path('save-company/', save_company, name='save-company'),
    path('get-companies/', get_companies, name='get-companies'),
    
    
    

]
