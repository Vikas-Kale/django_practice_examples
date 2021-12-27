from django.db import models

# Create your models here.

class Students(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField()
    stuAddress = models.CharField(max_length=70)
    