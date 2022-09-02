from django.db import models

# Create your models here.


class CountryMaster(models.Model):
    country_name=models.CharField(max_length=100)
    country_code=models.CharField(max_length=50)


class StateMaster(models.Model):
    State_name=models.CharField(max_length=100)
    state_code=models.CharField(max_length=50)
    country=models.ForeignKey(CountryMaster,on_delete=models.CASCADE)


class CityMaster(models.Model):
    city_name=models.CharField(max_length=100)
    state=models.ForeignKey(StateMaster,on_delete=models.CASCADE)

class Pincodemaster(models.Model):
    pin_code=models.IntegerField()
    city=models.ForeignKey(CityMaster,on_delete=models.CASCADE)