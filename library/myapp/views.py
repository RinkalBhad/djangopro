from django.shortcuts import render,redirect
from .models import*
from.form import*
# Create your views here.
def index(request):
    data=book.objects.all()
    
    return render(request,'index.html',{'data':data})


def addbook(request):
    if request.method=='POST':
        data=mynotes(request.POST)
        if data.is_valid():
            data.save()
            print("saved")
            return redirect("/")
    return render(request,'addbook.html')


def edit(request,id):
    b=book.objects.get(id=id)
    if request.method=='POST':
        data=mynotes(request.POST,instance=b)
        if data.is_valid():
            data.save()
            print("saved")
            return redirect("/")
    return render(request,'edit.html',{'b':b})


def delete(request,id):
    b=book.objects.get(id=id)
    book.delete(b)
    return redirect('/')