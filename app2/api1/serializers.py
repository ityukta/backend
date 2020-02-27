from rest_framework import serializers
from .models import Faculty, Type


class TypeSerializer(serializers.Serializer):
    type_description = serializers.CharField(max_length=1)

class InitialRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email_id = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=128)
    department = serializers.CharField(max_length=100)
    faculty_type = TypeSerializer(many=True)

    def create(self, validated_data):
        faculty = Faculty(
            name=validated_data['name'], email_id=validated_data['email_id'],
            password=validated_data['password'], department=validated_data['department'])
        faculty.save()
        faculty = Faculty.objects.get(email_id=validated_data['email_id'])
        faculty.faculty_type.add(Type.objects.get(
            type_description=validated_data['faculty_type'][0]['type_description']))
        return faculty
