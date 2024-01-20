from django.http import HttpResponse
from django.shortcuts import render
import datetime

def test(request):
   return HttpResponse("this is test function..")

def home(request):


    date=datetime.datetime.now()
    isActive=True
    name="rinkla"
    program=[
        "w.a.p to check even or odd",
        "prime number or not",
        "print 1 to 100"
    ]
    student={
        'name':"rinkal", 'clg':"xyz",'city':"rajkot"
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'program':program,
        'student':student
    }

    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")