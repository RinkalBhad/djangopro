from django.db import models

# Create your models here.
class usersignup(models.Model):
      firstname=models.CharField(max_length=10)
      lastname=models.CharField(max_length=10)
      username=models.EmailField()
      password=models.CharField(max_length=10)
      city=models.CharField(max_length=10)
      state=models.CharField(max_length=10)
      number=models.BigIntegerField()