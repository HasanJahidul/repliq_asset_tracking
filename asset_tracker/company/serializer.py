from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        depth = 4
        
        
        exclude = ['created_at', 'updated_at']
        def validate_name(self, data):
            if data.get("name"):
                name=data.get("name")
                if name.isdigit():
                    raise serializers.ValidationError("Name cannot be a number")
                if len(name)<3:
                    raise serializers.ValidationError("Name must be at least 3 characters")
                if name.isalpha():
                    raise serializers.ValidationError("Name must contain at least one letter")
        def validate_location(self, data):
            if data.get("location"):
                location=data.get("location")
                if location.isdigit():
                    raise serializers.ValidationError("Location cannot be a number")
                if len(location)<3:
                    raise serializers.ValidationError("Location must be at least 3 characters")
                if location.isalpha():
                    raise serializers.ValidationError("Location must contain at least one letter")
                
        def validate_ceo(self, data):
            if data.get("ceo"):
                ceo=data.get("ceo")
                if ceo.isdigit():
                    raise serializers.ValidationError("CEO cannot be a number")
                if len(ceo)<3:
                    raise serializers.ValidationError("CEO must be at least 3 characters")
                if ceo.isalpha():
                    raise serializers.ValidationError("CEO must contain at least one letter")                   
