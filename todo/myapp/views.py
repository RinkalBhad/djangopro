from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import*
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
   # if request.user.is_authenticated:
      # return redirect('home-page')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        data=User.objects.filter(username=username,password=password)
        if data:
            return redirect("todo")
        
        else:
            messages.error(request,'invalid username or password')
            return redirect('login')
    return render(request,'index.html')

def register(request):
   #if request.user.is_authenticated:
       #return redirect('home-page')
   if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get("email")
        password=request.POST.get("password")

        if len(password)<3:
            messages.error(request,'password is too short')
            return redirect('register')

       
        all_user=User.objects.filter(username=username)
        if  all_user:
            messages.error(request,'username already exists')
            return redirect('register')
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'user successfull , created login now')
        return redirect('login')
   return render(request,'register.html')
   

'''    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']

        data=User.objects.filter(username=username)
        if data:
           # messages.error(request,'username already exists')
            print("username already exists")
            return redirect('register')

        User.objects.create(username=username,password=password,email=email)

    return render(request,'register.html')'''
  
  
@login_required
def todopage(request):
    if request.method=='POST':
        task=request.POST['task']
        new_todo=todo(user=request.user,name=task) # this name is in model field
        new_todo.save()  


    all_data=todo.objects.filter(user=request.user) 
    return render(request,'todopage.html',{'all_data':all_data})

@login_required
def delete(request,name):
    st=todo.objects.get(name=name)
    todo.delete(st)
    return redirect("todo")

@login_required
def update(request,name):
    st=todo.objects.get(name=name)
    st.status=True
    st.save()
    return redirect("todo")


def userlogout(request):
    logout(request)
    return redirect("/")

