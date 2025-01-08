from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True,blank=True)


class scoresheet(models.Model):
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    maths=models.IntegerField()
    english=models.IntegerField()
    science=models.IntegerField()
