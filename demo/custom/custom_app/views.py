from django.shortcuts import render,redirect
from .models import CustomUser,scoresheet
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
# Create your views here.
def cusromRegister(request):
    if request.method=='POST':
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        email =request.POST['email']
        username =request.POST['username']
        password =request.POST['password']
        phone=request.POST['phone']
        data = CustomUser.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password,
                                        phone=phone)
        data.save()
        return HttpResponse("Successfully registered")
    
    else:
        return render(request,'customuser.html')
    
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            context={
                'message':"Invalid credentials"
            } 
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
    
def profile(request):
    data=CustomUser.objects.get(id=request.user.id)
    
    return render(request,'profile.html',{'details':data})

def Logout(request):
    auth.logout(request)
    return redirect(Login)


def profile_edit(request):
    data=CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        data.first_name=request.POST['firstname']
        data.last_name=request.POST['lastname']
        data.username=request.POST['username']
        data.email=request.POST['email']
        data.password=request.POST['password']
        data.phone=request.POST['phone']
        data.save()
        return redirect('profile')

    else:
        return render(request,'edit.html',{"data":data})
    

def marks(request):
    data=CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        maths=request.POST['maths']
        english=request.POST['english']
        science=request.POST['science']
        user_data = scoresheet.objects.create(user_id=data,maths=maths,english=english,science=science)
        user_data.save()
        return redirect('profile')
    else:
        return render(request,'score.html')


def view_mark(request):
    data=CustomUser.objects.get(id=request.user.id)
    mark = scoresheet.objects.filter(user_id=data.id)
    return render(request,'view_mark.html',{"marks":mark})

