from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Teacher(AbstractUser):
    department=models.CharField(max_length=50)
    phone=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.username
    
class Student(models.Model):
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Score(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    term=models.CharField(max_length=30)
    subject1=models.IntegerField()
    subject2=models.IntegerField()
    subject3=models.IntegerField()
    total=models.IntegerField()



