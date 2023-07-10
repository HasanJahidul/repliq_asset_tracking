from django.urls import path
from .views import *

urlpatterns = [
    path('save/', save_company, name='save-company'),
    path('get/', get_companies, name='get-companies'),
    
    
    

]
