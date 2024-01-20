from django.shortcuts import render,redirect
from .forms import*

# Create your views here.

def index(request):
    if request.method=='POST':
        newstud=studentForm(request.POST)
        if newstud.is_valid():
            newstud.save()
            print("your data has been saved..")

        else:
            print(newstud.errors)
    return render(request,"index.html")

def show(request):
    st=student.objects.all()
    return render(request,"show.html",{"st":st})

def update(request,id):
    data=student.objects.get(id=id)
    if request.method=='POST':
         h=hello(request.POST,instance=data)
         if  h.is_valid():
             h.save()
             print("data saved")
             return redirect("show")
             
         else:
             print(h.errors)
    return render(request,"update.html",{"data":data})


def delete(request,id):
    st=student.objects.get(id=id)
    student.delete(st)
    return redirect("show")

