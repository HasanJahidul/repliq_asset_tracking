from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer

# save employee
@api_view(['POST'])
def save_employee(request):
    try:
        data=request.data
        print(data)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Employee created successfully",
                "data": serializer.data
            })
        return Response({
            "status": "error",
            "message": "Employee not created",
            "errors": serializer.errors
        })
    
    except Exception as e:
        print(e)
        print(f"Error occurred during JSON serialization: {str(e)}")
        return Response({"message": "Employee not created"})