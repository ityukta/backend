from django.db import models
from django.utils.translation import gettext_lazy as _


class Type(models.Model):
    class TypeChoices(models.TextChoices):
        PRINCIPAL = 'P', _('Principal')
        HOD = 'H', _('Head of Department')
        CLASS_TEACHER = 'C', _('Class Teacher')
        SUBJECT_TEACHER = 'S', _('Subject Teacher')
        MENTOR = 'M', _('Mentor')
    type_id = models.AutoField(primary_key=True)
    type_description = models.CharField(
        max_length=1, choices=TypeChoices.choices)


class Publications(models.Model):
    publication_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    publication_detail = models.TextField()


class Workshops(models.Model):
    workshop_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    workshop_detail = models.TextField()


class FacultyQualification(models.Model):
    qualification_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    percentage = models.FloatField(max_length=4)
    graduation_year = models.PositiveSmallIntegerField(null=True)
    university = models.CharField(max_length=100)


class ResearchPaper(models.Model):
    research_paper_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    research_paper_details = models.TextField()


class SessionChair(models.Model):
    session_chair_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    session_chair_details = models.TextField()


class WorkExperience(models.Model):
    work_experience_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    duration = models.FloatField()


class AreaOfSpecialisation(models.Model):
    specialiation_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    specialiation_details = models.TextField()


class AcademicRole(models.Model):
    academic_role_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    academic_role_details = models.TextField()


class Faculty(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHERS = 'O', _('Others')

    class MartialStatusChoices(models.TextChoices):
        SINGLE = 'SI', _('Single')
        MARRIED = 'MA', _('Married')
        DIVORCED = 'DI', _('Divorced')
        WIDOWED = 'WI', _('Widowed')
        SEPERATED = 'SE', _('Seperated')

    class AssociationChoices(models.TextChoices):
        REGULAR = 'R', _('Regular')
        VISITING = 'V', _('Visiting')
        ADJUNCT = 'A', _('Adjunct')
        CONTRACT = 'C', _('Contract')

    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    department = models.CharField(max_length=100)
    phone = models.BigIntegerField(null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices, null=True, blank=True)
    marital_status = models.CharField(
        max_length=50, choices=MartialStatusChoices.choices, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    teacher_picture = models.ImageField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)

    publications = models.ManyToManyField(Publications)
    workshops = models.ManyToManyField(Workshops)
    faculty_qualificatio

    association_with_institution = models.CharField(
        max_length=20, choices=AssociationChoices.choices, null=True, blank=True)
    faculty_type = models.ManyToManyField(Type)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    approved = models.BooleanField(default=False)
    first_login = models.BooleanField(default=True)


class LoginAuthKey(models.Model):
    login_authkey_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    authkey = models.CharField(max_length=128)
    deleted = models.BooleanField(default=False)


class Class(models.Model):
    class SemChoices(models.IntegerChoices):
        FIRST = 1, _('First')
        SECOND = 2, _('Second')
        THIRD = 3, _('Third')
        FOURTH = 4, _('Fourth')
        FIFTH = 5, _('Fifth')
        SIXTH = 6, _('Sixth')
        SEVENTH = 7, _('Seventh')
        EIGTH = 8, _('Eigth')
    class_id = models.AutoField(primary_key=True)
    sem = models.IntegerField(choices=SemChoices.choices)
    sec = models.CharField(max_length=1)
    graduation_year = models.PositiveSmallIntegerField(null=True)
    department = models.CharField(max_length=50)
    classteacher_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10)
    batch = models.CharField(max_length=5)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=2)
    father_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    parent_mail = models.EmailField()
    permanent_address = models.TextField()
    current_address = models.TextField()
    c10th_res = models.FloatField()
    c12th_res = models.FloatField()
    student_pic = models.ImageField()
    deleted = models.BooleanField(default=False)


class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=10)
    credits = models.IntegerField()


class Fcs(models.Model):
    fcs_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Fcss(models.Model):
    fcss_id = models.AutoField(primary_key=True)
    fcs_id = models.ForeignKey(Fcs, on_delete=models.CASCADE)
    student_id = models.ManyToManyField(Student)


class Attendance(models.Model):
    a_id = models.AutoField(primary_key=True)
    fcss_id = models.ForeignKey(Fcss, on_delete=models.CASCADE)
    hour = models.IntegerField()
    date = models.DateField()
    status = models.BooleanField(default=False)


class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    fcs_id = models.ForeignKey(Fcs, on_delete=models.CASCADE)
    test_no = models.CharField(max_length=5)
    qp_pattern = models.FileField()


class Test_res(models.Model):
    testres_id = models.AutoField(primary_key=True)
    fcss_id = models.ForeignKey(Fcss, on_delete=models.CASCADE)
    # fcs_id = models.ForeignKey(Fcs, on_delete=models.CASCADE)
    marks = models.FileField()
