from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    # devices = serializers.StringRelatedField(many=True)
    # company = serializers.UUIDField()
    
    class Meta:
        model = Employee
        exclude = ['created_at', 'updated_at']
        
        
        