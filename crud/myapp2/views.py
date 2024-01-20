from django.shortcuts import render,redirect
from.forms import* 
from.models import*

# Create your views here.
def index(request):
    if request.method=='POST':
        user=stud(request.POST)
        if user.is_valid():
            user.save()
            print("saved")
        else:
            print(user.errors)
    return render(request,"index.html")

def show(request):
    st=student.objects.all()
    return render(request,"show.html",{'st':st})


def update(request,id):
    std=student.objects.get(id=id)
    if request.method=="POST":
        data=stud(request.POST,instance=std)
        if data.is_valid():
            data.save()
            print("updated")
            return redirect("show")
        else:
            print(data.errors)
    return render(request,"update.html",{"std":std})

def delete(request,id):
    data=student.objects.get(id=id)
    student.delete(data)
    return redirect("show")

def notes(request):
    if request.method=='POST':
        user=mynot(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            print("saved")

        else:
            print(user.errors)
    return render(request,'notes.html')