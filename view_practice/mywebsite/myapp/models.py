from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Students(models.Model):
    stuid = IntegerField()
    stuname = CharField(max_length=50)
    stuemail = CharField(max_length=50)
    stuaddress = CharField(max_length=50)
