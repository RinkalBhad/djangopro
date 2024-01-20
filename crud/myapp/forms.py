from django import forms
from.models import*

class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'


class hello(forms.ModelForm):
    class Meta:
        model=student
        fields=['username','email']