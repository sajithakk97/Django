from django.shortcuts import render,redirect
from .models import user
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index1.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        dob=request.POST['dob']
        occupation=request.POST['occupation']
        email=request.POST['email']
        address=request.POST['address']
        address2=request.POST['address2']
        areacode=request.POST['areacode']
        phone=request.POST['phone']
        post=request.POST['post']
        city=request.POST['city']
        upload=request.FILES['upload']
        data=user.objects.create(firstname=firstname,lastname=lastname,
                                 age=age,dob=dob,occupation=occupation,email=email,address=address,address2=address2,
                                 areacode=areacode,phone=phone,post=post,city=city,image=upload)
        data.save()
        return redirect(display)

    else:
        return render(request,'register.html')
    
def display(request):
    details=user.objects.all()
    return render(request,'display.html',{"display_data":details})
    



