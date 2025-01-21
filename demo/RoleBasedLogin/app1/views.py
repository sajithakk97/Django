from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout 
from django.contrib.auth.models import auth
from django.http import HttpResponse
from .models import CustomUser,Teacher,Student,Score

def index(request):
    return render(request,'index.html')

def teacher_register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        department = request.POST['department']
        salary = request.POST['salary']
        address = request.POST['address']
        data = CustomUser.objects.create_user(username=username,password=password,email=email,user_type="teacher")
        data.save()
        user = Teacher.objects.create(teacher_type_id=data,first_name=firstname,last_name=lastname,age=age,
                                      salary=salary,address=address,department=department)
        user.save()
        return redirect('login')
    else:
        return render(request,'teacher_register.html')
    
def student_register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        grade = request.POST['grade']
        gender = request.POST['gender']
        course = request.POST['course']
        address = request.POST['address']
        data = CustomUser.objects.create_user(username=username,password=password,email=email,user_type="student")
        data.save()
        user = Student.objects.create(student_type_id=data,first_name=firstname,last_name=lastname,course=course,
                                      gender=gender,address=address,grade=grade)
        user.save()
        return redirect('login')
    else:
        return render(request,'student_register.html')

    
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        admin_user = authenticate(request,username=username,password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return HttpResponse("success")
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.user_type=='teacher' and user.status=='accepted':
                return redirect('teacher')
            elif user.user_type=='student':
                return redirect('student')
        else:
            context={
                'message':"Invalid credentials"
            } 
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')

def student_page(request):
    return render(request,'student.html')   

def teacher_page(request):
    return render(request,'teacher.html')  
def view_students(request):
    students=Student.objects.all()
    return render(request,'view_students.html',{'students':students})
def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    data=Teacher.objects.get(teacher_type_id=user)
    print(data.first_name)
    return render(request,'profile.html',{'details':data})
def Logout(request):
    auth.logout(request)
    return redirect('login')

def add_mark(request,id):
    user=CustomUser.objects.get(id=request.user.id)
    taecher=Teacher.objects.get(teacher_type_id=user)
    data=Student.objects.get(id=id)
    if request.method=='POST':
        science=request.POST['science']
        english=request.POST['english']
        details=Score.objects.create(biology=science,english=english,student_id=data,teacher_id=taecher)
        details.save()
        return redirect(view_students)
    else:
        return render(request,'add_mark.html',{'student':data})
    
def view_mark(request):
    user=CustomUser.objects.get(id=request.user.id)
    data=Student.objects.get(student_type_id=user)
    score=Score.objects.filter(student_id=data)
    return render(request,'view_mark.html',{'details':score})

