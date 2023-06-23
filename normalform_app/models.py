from django.db import models

# Create your models here.
class Employe(models.Model):
    name=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()