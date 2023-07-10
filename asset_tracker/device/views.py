from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device
from .serializer import DeviceSerializer

# add devices
from rest_framework import viewsets

@api_view(['POST'])
def add_device(request):
    try:
        data=request.data
        print(data)
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Device created successfully",
                "data": serializer.data
            })
        return Response({
            "status": "error",
            "message": "Device not created",
            "errors": serializer.errors
        })
    
    except Exception as e:
        print(e)
        print(f"Error occurred during JSON serialization: {str(e)}")
        return Response({"message": "Device not created"})


# get all devices with company uid
@api_view(['POST'])
def get_devices(request):
    try:
        # get company uid from request body
        company_uid=request.data.get("company")
        # get devices
        devices=Device.objects.filter(company=company_uid)
        serializer=DeviceSerializer(devices,many=True)
        return Response({
            "status": "success",
            "message": "Devices retrieved successfully",
            "data": serializer.data
        })
    except Exception as e:
        print(e)
        return Response({"message": {str(e)}})
    
