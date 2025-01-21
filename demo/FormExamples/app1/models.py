from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
    company=models.CharField(max_length=100)
    district=models.CharField(max_length=100)

    def __str__(self):
        return self.name