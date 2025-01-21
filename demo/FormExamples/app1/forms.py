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