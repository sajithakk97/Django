from django.shortcuts import render,redirect
from .models import Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
def index(request):
    return render(request,'index.html')

def teacher_register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        department = request.POST['department']
        salary = request.POST['salary']
        address = request.POST['address']
        data = Teacher.objects.create(username=username,email=email,password=password,first_name=firstname,last_name=lastname,
                                      salary=salary,address=address,department=department)
        
        data.save()
        return HttpResponse("success")
    else:
        return render(request,'teacher_register.html')
    
def student_register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email'] 
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        course = request.POST['course']
        address = request.POST['address']
        data = Student.objects.create(username=username,password=password,email=email,first_name=firstname,
                                           last_name=lastname,course=course,address=address)
        data.save()
        
        return HttpResponse('success')
    else:
        return render(request,'student_register.html')

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context={'message':'Invalid User Credentials'}
        admin_user = authenticate(request,username=username,password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return render(request,'admin_page.html')
        
        if Teacher.objects.filter(username=username,password=password).exists():
            userdetail=Teacher.objects.get(username=request.POST['username'], password=password)
            if userdetail.password == request.POST['password'] :
                request.session['tid'] = userdetail.id
                return render(request,'teacher_home.html')
            else:
                return render(request,'login.html',{'message':'wait for admin approval'})

        elif Student.objects.filter(username=username,password=password).exists():
            userdetail=Student.objects.get(username=request.POST['username'], password=password)
            if userdetail.password == request.POST['password'] :
                request.session['cid'] = userdetail.id
                return render(request,'student_home.html')
            else:
                return render(request,'login.html',{'message':'wait for admin approval'})
       
            
        else:
            return render(request, 'login.html',{'message': 'Invalid Username or Password'})
    else:
        return render(request,'login.html')




def userprofile(request):
    if 'tid' in request.session:
        temp=request.session['tid']
        vpro=Teacher.objects.get(id=temp)
        return render(request,'teacher_profile.html',{'result':vpro})
    elif 'cid' in request.session:
        temp=request.session['cid']
        stud=Student.objects.get(id=temp)
        return render(request,'student_profile.html',{'result':stud})
    else:
        return redirect(logins)

    
def view_teachers(request):
    user=Teacher.objects.all()
    return render(request,'teacher.html',{'data':user})

def view_students(request):
    user=Student.objects.all()
    return render(request,'student.html',{'data':user})

def logout(request):
    try:
        del request.session['tid']
    except KeyError:
        pass
    return redirect('login')

def logout_student(request):
    try:
        del request.session['sid']
    except KeyError:
        pass
    return redirect('login')

def logout_admin(request):
    auth.logout(request)
    return redirect('login')

def set_status(request,id):
    data=Student.objects.get(id=id)
    if request.method=='POST':
        status=request.POST['status1']
        if status=='Accept':
            data.status='accepted'
        elif status=='Reject':
            data.status='rejected'
        data.save()
        return redirect(view_students)
    return redirect('view_students')


def set_status_teacher(request,id):
    data=Teacher.objects.get(id=id)
    if request.method=='POST':
        status=request.POST['status']
        if status=='Accept':
            data.status='accepted'
        elif status=='Reject':
            data.status='rejected'
        data.save()
        return redirect('view_teacher')
    return redirect('view_teacher')
   
        