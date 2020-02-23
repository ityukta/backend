from django.contrib import admin

# Register your models here.
from .models import(Class)
    admin.site.register(Class)

from .models import(Student)
    admin.site.register(Student)

from .models import(Subject)
    admin.site.register(Subject)

from .models import(fcs)
    admin.site.register(fcs)

from .models import(fcss)
    admin.site.register(fcss)

from .models import(Attendance)
    admin.site.register(Attendance)

from .models import(Tests)
    admin.site.register(Tests)

from .models import(Test_res)
    admin.site.register(Test_res)