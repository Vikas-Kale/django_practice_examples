from django.db import models

# Create your models here.

class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=150)
    stuemail = models.EmailField(max_length=150)
    address = models.CharField(max_length=150)

    