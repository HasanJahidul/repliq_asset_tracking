from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    devices = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Employee
        # fields = '__all__'
        depth = 4
        exclude = ['created_at', 'updated_at', 'company']
        