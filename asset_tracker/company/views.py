from rest_framework.decorators import api_view
from rest_framework.response import Response

from company.models import Company
from .serializer import CompanySerializer

# function to save company
@api_view(['POST'])
def save_company(request):
    try:
        data = request.data
        print(data)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Company created successfully",
                "data": serializer.data
            })
            
        else:
            return Response({
                    "status": "error",
                    "message": "Company not created",
                    "errors": serializer.errors
                })
            
        
        
        # serializer = CompanySerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"message": "Company created successfully"})
        # else:
        #     return Response({"message": "Company not created"})
    except Exception as e:
        print(e)
        print(f"Error occurred during JSON serialization: {str(e)}")
        return Response({"message": "Company not created"})

# function to get all companies
@api_view(['GET'])
def get_companies(request):
    try:
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response({"message": "Companies retrieved successfully", "data": serializer.data})
    except Exception as e:
        print(e)