from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    # a device can have many device_log
    device_log = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Device
        exclude = ['created_at', 'updated_at']