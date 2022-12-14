from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Candidate,Userdata,Imageupload,Employee
from .serializers import  GetcustomerDetailsserializer
from django.core.exceptions import ObjectDoesNotExist
from  faker import Faker
from rest_framework.viewsets import ModelViewSet
import random

import string
class FakeData(APIView):
    def post(self,request):

            f =Faker('en_IN')

            Userdata.objects.all().delete()
            for i in range(100):
                x = random.choices(string.ascii_uppercase, k=3)
                num4 = random.randint(0000, 9999)
                addhar = random.randint(000000000000,999999999999)
                name = f.name()
                last_name = f.last_name()
                email = f.email()
                phone = f.phone_number()
                # address = f.address()
                city = f.city()
                state=f.state()
                country=f.country()
                pan = "".join(x) + "P" +last_name[0].upper()+str(num4)+"D"

                user_obj = Userdata(name = name,phone = phone,city = city,state= state,country = country,pancard = pan
                                    ,aadharcard=addhar,emailid=email)
                user_obj.save()
                print(phone)
            return JsonResponse({})
class GetcustomerDetails(APIView):

    def post(self,request):
        serializer = GetcustomerDetailsserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pan_number = request.data.get("pan_number")
            try:
                obj = Userdata.objects.get(pancard=pan_number)#dajngo query
                res = {"name":obj.name,"phone":obj.phone,"email":obj.emailid,"city":obj.city,"state":obj.state,"country":obj.country
                   ,"pan_nunber":obj.pancard,"aadharcard":obj.aadharcard}
                return JsonResponse({"customers":res})
            except ObjectDoesNotExist as error:
                return JsonResponse({"Error":"User not exists in record"})

    def patch(self,request):
        phone = request.data.get("phone")
        pancard = request.data.get("pan_card")
        try:
            obj = Userdata.objects.get(pancard=pancard)
            prev_ph =obj.phone
            if obj:
                obj.phone= phone
                obj.save()
                res = {"name": obj.name, "phone": obj.phone, "email": obj.emailid, "city": obj.city, "state": obj.state,
                       "country": obj.country
                    , "pan_nunber": obj.pancard, "aadharcard": obj.aadharcard}
                return JsonResponse({"Updated deatils": res,"prev_ph":prev_ph})
        except ObjectDoesNotExist as err:
            return JsonResponse({"Error":"Given user not exists"})



    def get(self,request):
        from django.middleware import csrf
        token = csrf.get_token(request)
        return JsonResponse({"mag":token})


class Phoneno(APIView):
    def get(self,request):
        object1=Userdata.objects.filter(phone__startswith="89").all()
        D={}
        List_user=[]
        for obj in object1:
            res = {"name": obj.name, "phone": obj.phone, "email": obj.emailid, "city": obj.city, "state": obj.state,
                   "country": obj.country , "pan_nunber": obj.pancard, "aadharcard": obj.aadharcard}
            List_user.append(res)
        return JsonResponse({"result":List_user})

class Getuseremaila(APIView):
    def get(self, request):
        object1 = Userdata.objects.filter(emailid__icontains="a").all()
        D = {}
        List_user = []
        for obj in object1:
            res = {"name": obj.name, "phone": obj.phone, "email": obj.emailid, "city": obj.city, "state": obj.state,
                   "country": obj.country, "pan_nunber": obj.pancard, "aadharcard": obj.aadharcard}
            List_user.append(res)
        return JsonResponse({"result": List_user})

class GetCusts(APIView):
    def get(self,request):
        custs = Userdata.objects.all()
        cust_list =[]
        for obj in custs:
            res = {"name": obj.name, "phone": obj.phone, "email": obj.emailid, "city": obj.city, "state": obj.state,
                   "country": obj.country, "pan_nunber": obj.pancard, "aadharcard": obj.aadharcard}
            cust_list.append(res)

        return JsonResponse({"Customers":cust_list})


class ImageUploadView(APIView):
    def post(self,request):
        image=request.data.get("image")
        print("this is ",image)
        Imageupload(img=image).save()
        return JsonResponse({"result":"success"})

from rest_framework import viewsets
from .serializers import EmployeeSerializers
class EmpModelViewset(ModelViewSet):
    model = Employee
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()





