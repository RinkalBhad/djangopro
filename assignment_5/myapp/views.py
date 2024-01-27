from django.shortcuts import render
from .models import*
# Create your views here.


def index(request):
    data=Product_sub_cat.objects.all()
    return render(request,'index.html',{'data':data})
