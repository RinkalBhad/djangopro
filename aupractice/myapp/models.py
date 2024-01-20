from django.db import models

# Create your models here.
class usersignup(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    number=models.CharField(max_length=10)

class ussin(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)

class userinfo(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)