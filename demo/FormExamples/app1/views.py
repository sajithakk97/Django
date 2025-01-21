from django.shortcuts import render
from .forms import form1,EmployeeForm
from django.http import HttpResponse 
from .models import student

# Create your views here.
def index(request):
    if request.method=='POST':
        form=form1(request.POST)
        if form.is_valid():
            Name=form.cleaned_data['name']
            Age=form.cleaned_data['age']
            Address=form.cleaned_data['address']
            District=form.cleaned_data['district']
            data=student.objects.create(name=Name,age=Age,address=Address,district=District)
            data.save()
            return HttpResponse("Submitted!")
    else:
        form=form1()
        return render(request,'index.html',{'form':form})
    
def model_form(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form=EmployeeForm()
        return render(request,'model_form.html',{'form':form})