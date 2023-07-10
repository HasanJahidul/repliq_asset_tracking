from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    # company = serializers.StringRelatedField(many=False)
    # a employee can have many devices
    devices = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Employee
        exclude = ['created_at', 'updated_at']
        
        
        