from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Teacher,Student,Score
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
# Create your views here.
def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        department=request.POST['department']
        user=Teacher.objects.create_user(first_name=firstname,
                                    last_name=lastname,
                                    username=username,
                                    password=password,
                                    email=email,
                                    phone=phone,
                                    department=department)
        user.save()
        return redirect('login')
    else:
        return render(request,'register.html')
    
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('view')
        else:
            message="user not present"
            return render(request,'login.html',{'message':message})
    else:
        return render(request,'login.html')
    
def view_students(request):
    user=Teacher.objects.get(id=request.user.id)
    data=Student.objects.filter(teacher_id=user.id)
    return render(request,'display.html',{'details':data})

def add_student(request):
    user=Teacher.objects.get(id=request.user.id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        course=request.POST['course']
        stud=Student.objects.create(name=name,email=email,course=course,teacher_id=user)
        stud.save()
        return redirect(view_students)
    return render(request,'add_student.html')

def delete_student(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('view')

def edit_student(request,id):
    data=Student.objects.get(id=id)
    if request.method=='POST':
        data.name=request.POST['name']
        data.email=request.POST['email']
        data.course=request.POST['course']
        data.save()
        return redirect('view')
    else:
        return render(request,'edit_student.html',{'details':data})
    
def profile(request):
    data=Teacher.objects.get(id=request.user.id)
    return render(request,'profile.html',{'details':data})
def Logout(request):
    auth.logout(request)
    return redirect('login')

def edit_profile(request):
    data=Teacher.objects.get(id=request.user.id)
    if request.method=='POST':
        data.first_name=request.POST['firstname']
        data.last_name=request.POST['lastname']
        data.username=request.POST['username']
        data.email=request.POST['email']
        password=request.POST['password']
        data.set_password(password)
        data.phone=request.POST['phone']
        data.department=request.POST['department']
        data.save()
        return redirect('profile')
    else:
        return render(request,'edit_profile.html',{'details':data})
    
def search(request):
    user=Teacher.objects.get(id=request.user.id)
    data=Student.objects.filter(teacher_id=user.id)
    if request.method=='POST':
        text=request.POST['search']
        content=Student.objects.filter(name__icontains=text , teacher_id=user.id)
        return render(request,'display.html',{'details':content})
    else:
        return render(request,'display.html',{'details':data})
    
def marks(request,id):
    data=Student.objects.get(id=id)
    mark =Score.objects.filter(student_id=data)
    return render(request,'view_mark.html',{"marks":mark,'data':data})


def add_mark(request,id):
    try:
        stud = Student.objects.get(id=id)
        mark =Score.objects.filter(student_id=stud)
        print("starting",stud)
        if request.method=='POST':
            print("id = ",stud)
            term=request.POST['term']
            subject1=request.POST['subject1']
            subject2=request.POST['subject2']
            subject3=request.POST['subject3']
            total=int(subject1)+int(subject2)+int(subject3)
            print("total = ",total)
            mark_data = Score.objects.create(term=term,subject1=subject1,subject2=subject2,subject3=subject3,student_id=stud,total=total)
            mark_data.save()
            return render(request,'view_mark.html',{"marks":mark,'data':stud})
        else:
            print("stud ",stud)
            return render(request,'add_score.html',{'student':stud})
    except Student.DoesNotExist:
        return HttpResponse("Student not found.", status=404)
    
    
