from django.contrib import admin
from .models import Student,Teacher,Score
# Register your models here.


admin.site.register(Score)

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','email','teacher_id','course')
    fieldsets=((None,{'fields':('teacher_id','course')}),)
    search_fields=('name',)
    readonly_fields=('course',)

class TeacherAdmin(admin.ModelAdmin):
    search_fields=('username','email')


admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)


admin.site.site_header="Mark"