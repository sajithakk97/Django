from django.shortcuts import render
from django.http import HttpResponse
from .models import student

# Create your views here.
def ragister(request):
    if request.method=='POST':
        First_name=request.POST['first name']
        Last_name=request.POST['last name']
        Date_of_Birth=request.POST['dob']
        email=request.POST['email']
        Admission_number=request.POST['admission number']
        password1=request.POST['password1']
        password2=request.POST['password2']
        details=student.objects.create(FirstName=First_name,
                                       LastName=Last_name,
                                       DateOfBirth=Date_of_Birth,
                                       Email=email,
                                       AdmissionNumber=Admission_number,
                                       Password1=password1,
                                       Password2=password2)
        details.save()
        return HttpResponse("successfully refistered")

    return render(request,'register.html')
