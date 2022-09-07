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



class Yavatmaldata(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(District="Yavatmal")

class Mahapindata(models.Model):
    Name=models.CharField(max_length=100,default=None)
    Description=models.CharField(max_length=100,default="world_famous")
    BranchType=models.CharField(max_length=100,default=None)
    DeliveryStatus=models.CharField(max_length=100,default=None)
    Circle= models.CharField(max_length=100,default=None)
    District=models.CharField(max_length=100,default=None)
    Division=models.CharField(max_length=100,default=None)
    Region=models.CharField(max_length=100,default=None)
    Block=models.CharField(max_length=100,default=None)
    State=models.CharField(max_length=100,default=None)
    Country=models.CharField(max_length=100,default=None)
    Pincode=models.IntegerField(default=None)
    # atul=models.Manager()
    # yavdata=Yavatmaldata()


    class Meta:
        db_table="MahapinIndia"
    @classmethod
    def yavdata(self):
        return self.objects.filter(District="Yavatmal")

