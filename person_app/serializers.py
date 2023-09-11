from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Only alphabetic characters are allowed in the name field.")
        return value