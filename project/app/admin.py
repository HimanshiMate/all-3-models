from django.contrib import admin
from .models import Enroll,Student
from .models import Course,stu_register_course
from .models import Teacher,Subject

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)

admin.site.register(Course)
admin.site.register(stu_register_course)


admin.site.register(Enroll)
admin.site.register(Student)