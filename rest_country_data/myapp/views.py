from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url="https://restcountries.com/v3.1/all"
    stdata=requests.get(url)
    ss=stdata.json()
    return render(request,'index.html',{'ss':ss})