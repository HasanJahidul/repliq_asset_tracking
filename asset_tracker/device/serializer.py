from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    # belongs_to = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Device
        fields = '__all__'
        depth = 4