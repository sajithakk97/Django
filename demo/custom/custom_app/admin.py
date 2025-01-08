from django.contrib import admin
from .models import CustomUser,scoresheet

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(scoresheet)