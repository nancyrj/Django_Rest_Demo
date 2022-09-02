from django.urls import path
from . import views


urlpatterns = [
         path('save', views.Savedata.as_view(), name='index'),
         path('getdetailfrompincode', views.Pincode.as_view(), name='index'),
         path('hit', views.Hitindianpincode.as_view(), name='index'),
]