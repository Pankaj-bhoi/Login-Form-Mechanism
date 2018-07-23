from __future__ import unicode_literals
from django.db import models

class Reg(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    user = models.CharField(primary_key=True ,max_length=20)
    pwd = models.CharField(max_length=20,unique=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=10,unique=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20,blank=True,null=True)



