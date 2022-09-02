from rest_framework import serializers
from django.core.exceptions import ValidationError

class Pincodeserializer(serializers.Serializer):
    pin_code=serializers.IntegerField(required=True)

    def validate_pin_code(self, pin_code):
        if len(str(pin_code))==6 :
            return True
        raise ValidationError("Invalid PinCode Entered")

