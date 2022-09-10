from django.shortcuts import render
from app111.models import Userdata
from rest_framework.views import APIView
from django.http import JsonResponse
from .email import send_email_touser


# Create your views here.

class Email_send(APIView):
    def post(self,request):
        try:
            name = request.data.get("name")
            emailid = request.data.get("emailid")
            phone = request.data.get("phone")
            city = request.data.get("city")
            state = request.data.get("state")
            country = request.data.get("country")
            pancard = request.data.get("pancard")
            aadharcard = request.data.get("aadharcard")
            Userdata(name=name,emailid=emailid,phone=phone,city=city,
                     state=state,country=country,pancard=pancard,aadharcard=aadharcard).save()
            user_dict={"name":name,"emailid":emailid,"phone":phone,
                       "pancard":pancard,"aadharcard":aadharcard,"city":city,"state":state,"country":country}
            send_email_touser(email=emailid,user=name,user_dict=user_dict)
            return JsonResponse({"Succes":"Data saved succesfully"})
        except Exception as e:
            return JsonResponse({"error":"Error while saving the data {}".format(e)})
