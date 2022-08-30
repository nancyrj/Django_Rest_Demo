from django.contrib import admin

# Register your models here.

from .models import Candidate,Userdata

admin.site.register(Candidate)
admin.site.register(Userdata)
