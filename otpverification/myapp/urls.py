from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path("signup/",views.signup),
    path("verification/",views.verification,name='verification'),
    
]
