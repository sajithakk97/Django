from .models import employee
from django import forms
class form1(forms.Form):
    name=forms.CharField(max_length=50,label="Full Name",widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))
    age=forms.IntegerField(min_value=1,label='Age' ,widget=forms.TextInput(attrs={"placeholder":'Enter your age'}))
    address=forms.CharField(max_length=100,label='Address',widget=forms.TextInput(attrs={"placeholder":'Enter your address'}))
    district_choices=[('','select your district'),
                      ('malappuram','malapuram'),
                      ('kozhikode','kozhikode'),
                      ('palakkad','palakkad')]
    district=forms.ChoiceField(choices=district_choices,label='District',widget=forms.Select(attrs={'placeholder':'select your district'}))


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields=['name','salary','company','age','district']



#register form with validation function
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Password do not match")

        return cleaned_data
