from django.db import models

# Create your models here.
class student(models.Model):
    FirstName=models.CharField(max_length=50,null=True,blank=True) 
    LastName=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    DateOfBirth=models.DateField(null=True,blank=True)
    AdmissionNumber=models.IntegerField(null=True,blank=True)
    Password1=models.CharField(max_length=50,null=True,blank=True)
    Password2=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.FirstName
