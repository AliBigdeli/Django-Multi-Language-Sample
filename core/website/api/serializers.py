from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Author
from django.utils.translation import gettext_lazy as _

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Author
        fields = ['first_name','last_name']
        
        
    def validate(self, attrs):
        if attrs.get("first_name").isdigit():
            raise serializers.ValidationError({"detail":_("first_name cannot have numbers in it")})
        return super().validate(attrs)

