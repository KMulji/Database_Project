from django.contrib import admin

from .models import Student,Room,Course,Enrolled

admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Enrolled)


