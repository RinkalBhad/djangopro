from django.shortcuts import render,redirect
from.form import*
import random
from django.core.mail import send_mail
from otpverification import settings

# Create your views here.
otp=random.randint(1111,9999)
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        user=usersignupform(request.POST)
        if user.is_valid():
            user.save()
            print('save')

            global otp
            sub="Thank you"
            msg=f'Dear user\n\nfor giving your feedback\n your one time otp is {otp}\n thank you\n '
            fr=settings.EMAIL_HOST_USER
            re=[request.POST['username']]
            send_mail(subject=sub,message=msg,from_email=fr,recipient_list=re)
            return redirect("verification")
        else:
            print(user.errors)
    return render(request,'signup.html')

def verification(request):
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect("/")
        else:
            print("error")
    return render(request,'verification.html')