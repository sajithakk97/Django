from django.shortcuts import render
from .models import student,scoresheet
from django.http import HttpResponse
from .models import teacher,student,scoresheet,course

def register(request):
    if request.method=='POST':
        username =request.POST['username']
        password =request.POST['password']
        data = teacher.objects.create(username=username,password=password)
        data.save()
        return render(request,'view_student.html')
    
    else:
        return render(request,'register.html')
    

def add_student(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        
        stud=student.objects.create(username=name,course=course)
        stud.save()
        return render(request,'view_student.html')
    return render(request,'add_student.html')

    
