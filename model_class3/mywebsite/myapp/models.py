from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


