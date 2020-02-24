
from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Class)

admin.site.register(Student)

admin.site.register(Subject)

admin.site.register(fcs)

admin.site.register(fcss)

admin.site.register(Attendance)

admin.site.register(Tests)

admin.site.register(Test_res)
