from rest_framework import serializers
from .models import Device_Log

class Device_LogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device_Log
        fields = '__all__'
        depth = 4