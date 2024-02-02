from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    complated=models.BooleanField(default=False)
