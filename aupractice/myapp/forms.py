from django import forms
from.models import*

class sing(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'


class sin(forms.ModelForm):
    class Meta:
        model=ussin
        fields='__all__'

class usinfo(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'