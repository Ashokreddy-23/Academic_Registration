from django.contrib import admin
from .models import Course, Admin, Student, Faculty, FCourseMappings, Studentcourses

# Register your models here.
admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Studentcourses)
admin.site.register(FCourseMappings)