from django.db import models

# Create your models here.

class Candidate(models.Model):
        name = models.CharField(max_length=100)
        salary = models.IntegerField()
        cast = models.CharField(max_length=5)
        religion = models.CharField(max_length=10)
        mother_toung = models.CharField(max_length=50)

class Userdata(models.Model):
        name=models.CharField(max_length=100)
        emailid=models.EmailField()
        phone=models.IntegerField()
        city=models.CharField(max_length=100)
        state=models.CharField(max_length=100)
        country=models.CharField(max_length=100)
        pancard=models.CharField(max_length=15)
        aadharcard=models.IntegerField()