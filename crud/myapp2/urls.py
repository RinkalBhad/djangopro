from django.contrib import admin
from django.urls import path ,include
from myapp2 import  views

urlpatterns = [
    path('',views.index),
    path("show/",views.show,name="show"),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("notes/",views.notes),
   
]
