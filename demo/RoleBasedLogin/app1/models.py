from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type=models.CharField(max_length=20)
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    status=models.CharField(choices=status_choice,default='pending',max_length=100)
# Create your models here.
class Teacher(models.Model):
    teacher_type_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(blank=True,null=True)
    department=models.CharField(max_length=50)
    salary=models.IntegerField()
    address=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.first_name
    
class Student(models.Model):
    student_type_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    course=models.CharField(max_length=100)
    address=models.CharField(max_length=100,blank=True,null=True)
    gender=models.CharField(max_length=10)
    grade=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
    
class Score(models.Model):
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    english=models.IntegerField()
    biology=models.IntegerField()
    