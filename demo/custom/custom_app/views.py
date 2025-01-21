from django.shortcuts import render,redirect
from .models import CustomUser,scoresheet
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
import random
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def send_otp(email):
    otp=random.randint(100000,999999)
    send_mail('your otp code ',f'your otp code is {otp}','sajitharahman1997@gmail.com',[email],fail_silently=False,)
    return otp

def password_reset_request(request):
    if request.method=='POST':
        email=request.POST['email']
        try:
            user=CustomUser.objects.get(email=email)
            otp=send_otp(email)
            context={
                'email':email,
                'otp':otp
            }
            return render(request,'verify_otp.html',context)
        except CustomUser.DoesNotExist:
            messages.error(request,'email address not found')
    else:
        return render(request,'password_reset.html')
    return render(request,'password_reset.html')
            
def verify_otp(request):
    if request.method=='POST':
        email=request.POST.get('email')
        otpold=request.POST.get('otp')
        otp=request.POST.get('otp1')
        if otpold==otp:
            context={'otp':otp,
                     'email':email}
            return render(request,'new_password.html')
        else:
            messages.error(request,'Invalid otp')
    return render(request,'verify_otp.html')

def set_new_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        new_password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if new_password==confirm_password:
            try:
                data=CustomUser.objects.get(email=email)
                data.set_password(new_password)
                data.save()
                messages.success(request,'password has been reset successfully')
                return redirect('login')
            except data.DoesNotExist:
                messages.error(request,'password doesnot match')
        return render(request,'new_password.html',{'email':email})
    return render(request,'new_password.html',{'email':email})
                



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

def delete(request,id):
    data=scoresheet.objects.get(id=id)
    data.delete()
    return redirect('profile')
def score_edit(request,id):
    data=scoresheet.objects.get(id=id)
    if request.method == 'POST':
        data.maths=request.POST['maths']
        data.english=request.POST['english']
        data.science=request.POST['science']
        data.save()
        return redirect('profile')
    else:
        return render(request,'edit_score.html',{'details':data})



