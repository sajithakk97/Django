from django.contrib import admin
from .models import course,student,scoresheet,teacher

admin.site.register(student)
admin.site.register(course)
admin.site.register(scoresheet)
admin.site.register(teacher)