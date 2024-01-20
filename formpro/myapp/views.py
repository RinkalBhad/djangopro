from django.shortcuts import render
from .forms import*

# Create your views here.
def index(request):
    if request.method=="POST":
        obj=stud(request.POST)
        if obj.is_valid():
            obj.save()
            print("saved")

        else:
            print(obj.errors)
    return render(request,"index.html")
