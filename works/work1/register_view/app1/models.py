from django.db import models

# Create your models here.
class student(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    Date_of_birth=models.DateField()

    def __str__(self):
        return self.First_name

