from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
  
    path("",views.index,name='login'),
    path("register/",views.register,name='register'),
    path("todopage/",views.todopage,name='todo'),
    path("delete/<str:name>/",views.delete),
    path("update/<str:name>/",views.update),
    path("userlogout/",views.userlogout),
]
