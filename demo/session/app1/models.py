from django.db import models

class Teacher(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.IntegerField()
    address=models.CharField(max_length=100,blank=True,null=True)
    status_choices=(('accepted','accepted'),('pending','pending'),('rejected','rejected'))
    status=models.CharField(choices=status_choices,default='pending',max_length=100)

    def __str__(self):
        return self.first_name
    
class Student(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    course=models.CharField(max_length=100)
    address=models.CharField(max_length=100,blank=True,null=True)
    status_choices=(('accepted','accepted'),('pending','pending'),('rejected','rejected'))
    status=models.CharField(choices=status_choices,default='pending',max_length=100)
    def __str__(self):
        return self.first_name
    
