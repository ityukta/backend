from rest_framework import serializers
from .models import Faculty, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['type_description']


class InitialRequestSerializer(serializers.ModelSerializer):
    faculty_type = TypeSerializer(many=True)

    class Meta:
        model = Faculty
        fields = ['faculty_id', 'name', 'email_id',
                  'password', 'department', 'faculty_type']

    def create(self, validated_data):
        print(validated_data)
        faculty = Faculty(
            name=validated_data['name'], email_id=validated_data['email_id'],
            password=validated_data['password'], department=validated_data['department'])
        faculty.save()
        faculty = Faculty.objects.get(email_id=validated_data['email_id'])
        faculty.faculty_type.add(Type.objects.get(
            type_description=validated_data['faculty_type'][0]['type_description']))
        # faculty.save()
        return faculty