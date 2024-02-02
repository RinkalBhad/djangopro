from django.db import models

# Create your models here.
class userdata(models.Model):
    firstname=models.CharField(max_length=10)
    email=models.EmailField()
    city=models.CharField(max_length=10)
