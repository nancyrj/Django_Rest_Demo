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
    # pan_number=serializers.CharField(required=True,validators=[valid_pan_provided])
    pan_number=serializers.CharField(required=True)
    def validate_pan_number(self,pan_number):
        if (pan_number[3] == "P"):
            return True
        raise ValidationError("invalid pancard*******")
