from rest_framework import serializers
from django.core.exceptions import ValidationError
import re


def valid_aadhar_provided(addhar):
    if len(str(addhar))==12:
        return True
    raise ValidationError("invalid aadhar")


def valid_pan_provided(pan):
    if (pan[3]=="P"):
        return True
    raise ValidationError("invalid pancard")

class GetcustomerDetailsserializer(serializers.Serializer):
    # name=serializers.CharField(required=True)
    # phone=serializers.IntegerField(required=True)
    # email=serializers.EmailField(required=True)
    # city=serializers.CharField(required=True)
    # state=serializers.CharField(required=True)
    # country=serializers.CharField(required=True)
    # adharcard=serializers.IntegerField(required=True)
    pan_number=serializers.CharField(required=True,validators=[valid_pan_provided])