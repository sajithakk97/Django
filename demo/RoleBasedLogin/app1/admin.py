from django.contrib import admin
from .models import Teacher,Student,Score,CustomUser
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Score)
admin.site.register(CustomUser)


