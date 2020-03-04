from rest_framework import serializers
from .models import Faculty, Type, LoginAuthKey


class APIResponse():
    def __init__(self, code, msg, data, authkey):
        self.status_code = code
        self.status_message = msg
        self.data = data
        self.authkey = authkey


class APIResponseSerializer(serializers.Serializer):
    status_code = serializers.IntegerField(allow_null=True, read_only=True)
    status_message = serializers.CharField(
        max_length=100, allow_null=True, read_only=True)
    authkey = serializers.CharField(allow_null=True, read_only=True)


class TypeSerializer(serializers.Serializer):
    type_description = serializers.CharField(max_length=1)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class InitialRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email_id = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=128)
    department = serializers.CharField(max_length=100)
    faculty_type = TypeSerializer(many=True)


class initialRegistrationResponseSerilaizer(APIResponseSerializer):
    data = InitialRequestSerializer()

    def create(self, validated_data):
        faculty = Faculty(
            name=validated_data['data']['name'], email_id=validated_data['data']['email_id'],
            password=validated_data['data']['password'], department=validated_data['data']['department'])
        faculty.save()
        faculty = Faculty.objects.get(
            email_id=validated_data['data']['email_id'])
        faculty.faculty_type.add(Type.objects.get(
            type_description=validated_data['data']['faculty_type'][0]['type_description']))
        return APIResponse(code=200, msg="OK", data=faculty, authkey=None)


class PublicationsSerializer(serializers.Serializer):
    publication_detail = serializers.CharField(max_length=500)


class WorkshopsSerializer(serializers.Serializer):
    workshop_detail = serializers.CharField(max_length=500)


class FacultyQualificationSerializer(serializers.Serializer):
    degree = serializers.CharField(max_length=100)
    branch = serializers.CharField(max_length=100)
    institution = serializers.CharField(max_length=100)
    percentage = serializers.FloatField()
    graduation_year = serializers.IntegerField()
    university = serializers.CharField(max_length=100)


class ResearchPaperSeializer(serializers.Serializer):
    research_paper_details = serializers.CharField(max_length=500)


class SessionChairSerializer(serializers.Serializer):
    session_chair_details = serializers.CharField(max_length=500)


class WorkExperienceSerializer(serializers.Serializer):
    designation = serializers.CharField(max_length=100)
    organization = serializers.CharField(max_length=100)
    duration = serializers.FloatField()


class AreaOfSpecialisationSerializer(serializers.Serializer):
    specialisation_details = serializers.CharField(max_length=500)


class AcademicRoleSerializer(serializers.Serializer):
    academic_role_details = serializers.CharField(max_length=500)


class LoginSerializer(serializers.Serializer):
    email_id = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=128, write_only=True)

    name = serializers.CharField(max_length=100, read_only=True)
    faculty_id = serializers.IntegerField(read_only=True)
    department = serializers.CharField(max_length=100, read_only=True)
    phone = serializers.IntegerField(read_only=True)
    date_of_joining = serializers.DateField(read_only=True)
    experience = serializers.IntegerField(read_only=True)
    date_of_birth = serializers.DateField(read_only=True)
    gender = serializers.CharField(max_length=1, read_only=True)
    marital_status = serializers.CharField(max_length=50, read_only=True)
    address = serializers.CharField(read_only=True)
    teacher_picture = serializers.ImageField(read_only=True)
    designation = serializers.CharField(max_length=100, read_only=True)
    publications = PublicationsSerializer(read_only=True, many=True)
    workshops = WorkExperienceSerializer(read_only=True, many=True)
    faculty_qualifications = FacultyQualificationSerializer(
        read_only=True, many=True)
    research_papers = ResearchPaperSeializer(read_only=True, many=True)
    session_chairs = SessionChairSerializer(read_only=True, many=True)
    work_experiences = WorkExperienceSerializer(read_only=True, many=True)
    area_of_specialisation = WorkExperienceSerializer(
        read_only=True, many=True)
    academic_roles = AcademicRoleSerializer(read_only=True, many=True)
    association_with_institution = serializers.CharField(
        max_length=20, read_only=True)
    faculty_type = TypeSerializer(read_only=True, many=True)
    first_login = serializers.BooleanField(read_only=True)

    def validate(self, data):
        try:
            f = Faculty.objects.get(
                email_id=data['email_id'], password=data['password'])
        except Faculty.DoesNotExist:
            raise serializers.ValidationError(
                {"other": "Incorrect email_id or password"})
        try:
            f = Faculty.objects.get(
                email_id=data['email_id'], password=data['password'], approved=True)
        except Faculty.DoesNotExist:
            raise serializers.ValidationError(
                {"other": "Account not yet approved."})
        return data


class LoginResponseSerializer(APIResponseSerializer):
    data = LoginSerializer()

    def create(self, validated_data):
        f = Faculty.objects.get(
            email_id=validated_data['data']['email_id'], password=validated_data['data']['password'], approved=True)
        la = LoginAuthKey.objects.create(faculty_id=f, authkey='123')

        return APIResponse(code=200, msg="OK", data=f, authkey=la.authkey)

    def update(self, instance, validate_data):
        pass


class CompleteRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    faculty_id = serializers.IntegerField(write_only=True)
    phone = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    experience = serializers.IntegerField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField(max_length=1)
    marital_status = serializers.CharField(max_length=50)
    address = serializers.CharField()
    teacher_picture = serializers.ImageField()
    designation = serializers.CharField(max_length=100)
    publications = PublicationsSerializer(many=True, allow_null=True)
    workshops = WorkExperienceSerializer(many=True, allow_null=True)
    faculty_qualifications = FacultyQualificationSerializer(
        many=True, allow_null=True)
    research_papers = ResearchPaperSeializer(many=True, allow_null=True)
    session_chairs = SessionChairSerializer(many=True, allow_null=True)
    work_experiences = WorkExperienceSerializer(many=True, allow_null=True)
    area_of_specialisation = WorkExperienceSerializer(many=True)
    academic_roles = AcademicRoleSerializer(many=True, allow_null=True)
    association_with_institution = serializers.CharField(max_length=20)


# class CompleteRegistrationResponseSerializer(APIResponseSerializer):
#     data = CompleteRegistrationSerializer()
#     def create(self, validated_data):
        
