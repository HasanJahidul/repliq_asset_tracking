from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device_Log
from .serializer import Device_LogSerializer

@api_view(['POST'])
def save_device_log(request):
    try:
        data=request.data
        print(data)
        serializer = Device_LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Device_Log created successfully",
                "data": serializer.data
            })
        return Response({
            "status": "error",
            "message": "Device_Log not created",
            "errors": serializer.errors
        })
    
    except Exception as e:
        print(e)
        print(f"Error occurred during JSON serialization: {str(e)}")
        return Response({"message": "Device_Log not created"})

@api_view(['POST'])
def get_device_logs(request):
    try:
        # get device uid from request body
        device_uid=request.data.get("device_uid")
        # get device_log
        device_log=Device_Log.objects.filter(device=device_uid)
        serializer=Device_LogSerializer(device_log,many=True)
        return Response({
            "status": "success",
            "message": "Device_Log retrieved successfully",
            "data": serializer.data
        })
    except Exception as e:
        print(e)
        return Response({"message": {str(e)}})
