from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        FirstName=request.POST['first name']
        LastName=request.POST['last name']
        Email=request.POST['email']
        Password=request.POST['password']
        DateOfBirth=request.POST['date of birth']
        data=student.objects.create(First_name=FirstName,Last_name=LastName,Email=Email,Password=Password,Date_of_birth=DateOfBirth)
        data.save()
        message="Successfully registered"
        return redirect('register')
    else:
        return render(request,'register.html')
    
def display_data(request):
    display_details=student.objects.all()
    context={'details':display_details}
    return render(request,'display.html',context)

def delete_data(request,ID):
    delete_data=student.objects.get(id=ID)
    delete_data.delete()
    return redirect(display_data)

def edit_data(request,ID):
    edit_data=student.objects.get(id=ID)
    if request.method=='POST':
        edit_data.First_name=request.POST['first name']
        edit_data.Last_name=request.POST['last name']
        edit_data.Email=request.POST['email']
        edit_data.Password=request.POST['password']
        edit_data.Date_of_birth=request.POST['date of birth']
        edit_data.save()
        return redirect(display_data)
    else:
        context={"data":edit_data}
        return render(request,'edit.html',context)
