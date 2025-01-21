from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    class_session = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.class_session} - {self.date} - {'Present' if self.is_present else 'Absent'}"
