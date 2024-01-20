from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField()
