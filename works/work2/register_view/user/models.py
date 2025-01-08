from django.db import models
# Create your models here.
class user(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField()
    dob=models.DateField()
    occupation=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.TextField()
    address2=models.TextField()
    areacode=models.IntegerField()
    phone=models.IntegerField()
    post=models.IntegerField()
    city=models.CharField(max_length=50)
    image=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.firstname
    
