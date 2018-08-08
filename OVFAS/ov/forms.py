from django import forms
from django.contrib.auth.models import User

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['registration_no']
        