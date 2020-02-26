from django.contrib.auth.models import Faculty
from rest_framework import serializers
from .models import Faculty
class InitialRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'name', 'email_id', 'password', 'department', 'faculty_type']
    