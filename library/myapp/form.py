from django import forms
from.models import*

class mynotes(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'