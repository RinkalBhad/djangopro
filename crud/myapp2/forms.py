from django import forms
from.models import*

class stud(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"

class mynot(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'