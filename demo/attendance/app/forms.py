from django import forms
from .models import Attendance, Student

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'class_session', 'date', 'is_present']

class AttendanceMarkForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.HiddenInput())
    is_present = forms.BooleanField(required=False, widget=forms.CheckboxInput())
