from .views import Email_send
from django.urls import path

urlpatterns = [
         path('email_send', Email_send.as_view(), name='index'),
    ]
