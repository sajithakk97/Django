from django.db import models
class scoresheet(models.Model):
    grade=models.CharField(max_length=10)

    def __str__(self):
        return self.grade

class course(models.Model):
    course_name=models.CharField(max_length=50)
    year=models.CharField(max_length=20)

    def __str__(self):
        return self.course_name
    
class student(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    marks=models.OneToOneField(scoresheet,on_delete=models.CASCADE,related_name='student')
    course=models.ManyToManyField(course,related_name='course')

    def __str__(self):
        return self.username
    
class teacher(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username
