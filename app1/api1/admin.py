
from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Class)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Fcs)
admin.site.register(Fcss)
admin.site.register(Attendance)
admin.site.register(Tests)
admin.site.register(Test_res)
