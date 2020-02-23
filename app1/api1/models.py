from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    
class Class(models.Model):
    class_id        = models.AutoField(primary_key=True)
    sem             = models.IntegerField(1)
    sec             = models.CharField(max_length=1)
    grad_year       = models.IntegerField()
    department      = models.CharField(max_length=20)
    classteacher_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)

class Student(models.Model):
    student_id          = models.AutoField(primary_key =True)
    name                = models.CharField(max_length=100)
    usn                 = models.CharField(max_length=10)
    batch               = models.CharField(max_length=5)
    class_id            = models.ForeignKey(Class ,on_delete=models.CASCADE)
    blood_group         = models.CharField(max_length=2)
    father_name         = models.CharField(max_length=100)
    phone_no            = models.BigIntegerField()
    parent_mail         = models.EmailField()
    permanent_address   = models.TextField()
    current_address     = models.TextField()
    10th_res            = models.FloatField()
    12th_res            = models.FloatField()
    student_pic         = models.ImageField()

class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=10)
    credits = models.IntegerField()

class fcs(models.Model):
    fcs_id = models.AutoField(primary_key=True)
    Faculty_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    class_id = models.ForeignKey(class,on_delete=models.CASCADE)
    sub_id =models.ForeignKey(Subject,on_delete=models.CASCADE)

class fcss(models.Model):
    fcss_id = models.AutoField(primary_key=True)
    fcs_id =models.ForeignKey(fcs,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    
class Attendance(models.Model):
    a_id = models.AutoField(primary_key=True)
    fcss_id models.ForeignKey(fcss,on_delete=models.CASCADE)
    hour = models.IntegerField()
    date = models.DateField()
    status = models.SmallIntegerField()

class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    fcs_id = models.ForeignKey(fcs,on_delete=models.CASCADE)
    test_no = models.CharField(max_length=5)
    qp_pattern = models.FileField()

class Test_res(models.Model):
    testres_id = models.AutoField(primary_key=True)
    fcss_id = models.ForeignKey(fcss,on_delete=models.CASCADE)
    fcs_id= models.ForeignKey(fcs,on_delete=models.CASCADE) 
    marks = models.FileField()

