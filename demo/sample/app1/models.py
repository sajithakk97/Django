from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    image=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.first_name