from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

class mynotes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    titl=models.CharField(max_length=10)
    myfile=models.FileField(upload_to='Media')
    comments=models.TextField()