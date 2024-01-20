from django.shortcuts import render,redirect
from.models import*
from django.contrib.auth import logout
from django.contrib import messages
from.forms import*

# Create your views here.

def index(request):
    if request.method=='POST':
         unm=request.POST['username']
         pwd=request.POST['password']

         data=usersignup.objects.filter(username=unm,password=pwd)
         if data:
             messages.info(request, "item saved !!!")
             print("login successfull")
             
             request.session['user']=unm
             return redirect("home")
         else:
             print("invlaid username or password")

    return render(request,'index.html')


def signup(request):
    if request.method=='POST':
        user=sing(request.POST)
        if user.is_valid():
            user.save()
            print("saved")
            messages.info(request, "item saved !!!")
            return redirect('home')
        else:
            print(user.errors)
    return render(request,'signup.html')

def home(request):
    data=request.session.get('user')
    return render(request,'home.html',{'data':data})

def userlogout(request):
    logout(request)
    messages.info(request, "item removed !!!")
    return redirect("/") 


def another(request):
    if request.method=='POST':
        user=sin(request.POST)
        if user.is_valid():
        
             username=user.cleaned_data['username']
             email=user.cleaned_data['email']

             if ussin.objects.filter(email=ussin.email).exists():
                messages.info(request,"email alreaddy taken")
                return redirect("another")
            
             elif ussin.objects.filter(username=ussin.username).exists():
                messages.info(request,"username already taken ")
                return redirect("another")
            
             else:
                print("signup succesfully")
                user.save()

        else:
            print(user.errors)

    return render(request,'another.html')


def forsignup(request):
    if request.method=='POST':
        user=usinfo(request.POST)
        
        if user.is_valid():
            username=user.cleaned_data['username']
            email=user.cleaned_data['email']
            password=user.cleaned_data['password']
            password2=user.cleaned_data['password2']

            if password==password2:
                if userinfo.objects.filter(username=username).exists():
                    messages.info(request,'username already exists ')
                    return redirect(forsignup)
                
                elif userinfo.objects.filter(email=email).exists():
                    messages.info(request,'email already exists')
                    return redirect(forsignup)
                
                else:
                    user.save()
                    messages.info(request,"signup successfully done")
            else:
                messages.info(request,'password are not matches')
                return redirect(forsignup)
            
        else:
            print(user.errors)

    return render(request,'forsignup.html')