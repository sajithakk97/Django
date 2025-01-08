from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
from django.contrib.auth.models import User

# Create your views here.message
def function1(request):
    return HttpResponse("this is my first project")


def pass_value(request,val):
    return HttpResponse(val)
def add(request,num1,num2):
    return HttpResponse(f"sum is {num1+num2} ")

def count_vowels(request,string):
    list1=['a','e','i','o','u']
    count=0
    for i in string.lower():
        if i in list1: 
            count+=1
    return HttpResponse(f"number of vowels in {string} is {count}")



def register(request):
    if request.method=='POST':
        first_name=request.POST['first name']
        if student.objects.filter(first_name=first_name):
            return render(request,'index.html',{"message":"first name already exists"})
        last_name=request.POST['last name']
        Email=request.POST['email']
        Password=request.POST['password']
        image=request.FILES['img']
        data = student.objects.create(first_name=first_name,last_name=last_name,email=Email,password=Password,image=image)
        data.save()
        return redirect(display)
    else:
        return render(request,'index.html')
    
def display(request):
    details=student.objects.all()
    return render(request,'display.html',{"display_data":details})


def data_delete(request,id):
    dta_to_be_delete=student.objects.get(id=id)
    dta_to_be_delete.delete()
    return redirect(display)

def data_edit(request,id):
    data_to_be_edit=student.objects.get(id=id)
    if request.method=='POST':
        data_to_be_edit.first_name=request.POST['first name']
        data_to_be_edit.last_name=request.POST['last name']
        data_to_be_edit.email=request.POST['email']
        data_to_be_edit.password=request.POST['password']
       
        data_to_be_edit.save()
        return redirect(display)
    
    else:
        context={"data":data_to_be_edit}
        return render(request,'edit.html',context)
    

def index(request):
    return render(request,'index2.html')

