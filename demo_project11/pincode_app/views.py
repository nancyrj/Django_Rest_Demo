from django.shortcuts import render
from .models import CountryMaster,StateMaster,CityMaster,Pincodemaster
from rest_framework.views import APIView
from  faker import Faker
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .serializer import Pincodeserializer
import requests as req
# from django.conf import settings
from demo_project11.settings import *

PIN_CODE_API_URL=config.get("PICODE_API","API_URL")



# Create your views here.


class Savedata(APIView):
    def post(self,request):
        f=Faker('en_IN')
        l =[]
        s = set()
        sc = set()
        ct = []
        for i in range(10):
             country=f.country()
             country_code=f.country_code()
             state= f.state()
             # l.append(state)
             s.add(state)
             state_code = state[0:4].upper()
             sc.add(state_code)
             city= f.city()
             ct.append(city)

             # cm=CountryMaster(country_name=country,country_code=country_code).save()
             # StateMaster.objects.all().delete()
        st_obj = StateMaster.objects.all()
        Pincodemaster.objects.all().delete()
        for st in st_obj:
            for j in range(len(ct)):
                pass
                # CityMaster(city_name=ct[j],state=st).save()
        # print(len(list(s)))
        for obj in CityMaster.objects.all():
            import random
            Pincodemaster(pin_code=random.randrange(111111,999999,6),city=obj).save()
        # print(len(list(sc)))
        # for i in range(len(list(s))):
        #     sl = list(s)
        #     sc = sl[i]
        #     in_obj = CountryMaster.objects.get(country_code="IN")
        #     StateMaster(State_name=sl[i], state_code=sc[0:3], country=in_obj).save()

        return JsonResponse({"country_data":l})

class Pincode(APIView):
    def post(self,request):
        serializer = Pincodeserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                pin_code=request.data.get("pin_code")
                obj=Pincodemaster.objects.get(pin_code=pin_code)
                city_name=str(obj.city.city_name)
                state_name=obj.city.state.State_name
                state_code=obj.city.state.state_code
                country_name=obj.city.state.country.country_name
                country_code=obj.city.state.country.country_code
                dict_pincode={"pin_code":pin_code,"city_name":city_name,"State_name":state_name,"state_code":state_code,
                              "country_name":country_name,"country_code":country_code}
                return JsonResponse({"key":dict_pincode})
            except ObjectDoesNotExist as err:
                return JsonResponse({"Error_msg":"pincode is wrongg!"},status=400)
            except:
                return JsonResponse({"key":"exception"})


class Hitindianpincode(APIView):
    def post(self,request):
        pincode=request.data.get("Pincode")
        resp=req.get(url=PIN_CODE_API_URL+"/{}".format(pincode))
        # print(resp.json())
        return JsonResponse({"result":resp.json()})








