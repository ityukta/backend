from rest_framework import serializers
from .models import *


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
        print(validated_data)
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
    authkey = serializers.CharField(max_length=10)

    # def validate(self,data):
    #         try :
    #             f =LoginAuthKey.objects.get(
    #                 faculty_id=data['faculty_id'],authkey= data['authkey'],deleted = False)
    #         except LoginAuthKey.DoesNotExist:
    #             raise serializers.ValidationError(
    #         {"other ":"authorization required"})
    #         return data
    
class CompleteRegistrationResponseSerializer(APIResponseSerializer):
    data = CompleteRegistrationSerializer()
    def create(self, validated_data):
        print(validated_data)
        f= Faculty.objects.get(
            faculty_id=validated_data['data']['faculty_id']
        )
        print(f.publications)
        p = Publications(publication_detail= validated_data["data"]["publications"][0]["publication_detail"])
        p.save()
        w = Workshops(workshop_detail= validated_data["data"]["workshops"][0]["workshop_detail"])
        w.save()
        fq = FacultyQualification(degree = validated_data["data"]["faculty_qualifications"][0]["degree"] , 
                branch = validated_data["data"]["faculty_qualifications"][0]["branch"],
                institution = validated_data["data"]["faculty_qualifications"][0]["institution"],
                percentage = validated_data["data"]["faculty_qualifications"][0]["percentage"],
                graduation_year = validated_data["data"]["faculty_qualifications"][0]["gradution_year"]
                university = validated_data["data"]["faculty_qualifications"][0]["university"])
        fq.save()
        rp = ResearchPaper(research_paper_details = validated_data["data"]["research_papers"]["research_paper_details"])
        rp.save()
        sc = SessionChair(session_chair_details = validated_data["data"]["session_chairs"]["session_chair_details"])
        sc.save()
        we = WorkExperience(designation= validated_data["data"]["work_experiences"]["designation"],
                organization =validated_data["data"]["work_experiences"]["organisation"],
                duration = validated_data["data"]["work_experiences"]["duration"])
        we.save()
        aos = AreaOfSpecialisation(specialisation_details = validated_data["data"]["area_of_specialisation"]["specialisation_details"])
        aos.save()
        ar = AcademicRole(academic_role_details = validated_data["data"]["academic_roles"]["academic_role_details"])
        ar.save()
        f.phone = validated_data["data"]["phone"]
        f.date_of_joining = validated_data["data"]["date_of_joining"]
        fexperience = validated_data["data"]["experience"]
        f.date_of_birth= validated_data["data"]["date_of_birth"]
        f.gender = validated_data["data"]["gender"]
        f.marital_status=validated_data["data"]["maritial_status"]
        f.address=validated_data["data"]["address"]
        f.teacher_picture=validated_data["data"]["teacher_picture"]
        f.designation=validated_data["data"]["designation"]
        f.publications.add(p)
        f.workshops.add(w)
        f.faculty_qualifications.add(fq)
        f.research_papers.add(rq)
        f.session_chairs.add(sc)
        f.work_experiences.add(we)
        f.area_of_specialisation.add(aos)
        f.academic_roles.add(ar)
        f.save()
        return APIResponse(code=200, msg="OK", data=f, authkey=None)    


        
