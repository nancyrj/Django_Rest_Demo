from django.urls import path
from . import views


urlpatterns = [
         path('save', views.FakeData.as_view(), name='index'),
         path('cust_details', views.GetcustomerDetails.as_view(), name='index'),
         path('cust_no', views.Phoneno.as_view(), name='index'),
         path('cust_mail_a', views.Getuseremaila.as_view(), name='index'),
         path('cust_all', views.GetCusts.as_view(), name='index'),
         path('image_upload', views.ImageUploadView.as_view(), name='index'),]

