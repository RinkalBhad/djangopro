from django import forms
from .models import*

class stud(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"