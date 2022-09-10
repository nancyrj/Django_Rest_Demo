from django.core.management.base import BaseCommand
import requests as reqq
from pincode_app.models import Mahapindata
from demo_project11.settings import *

PIN_CODE_API_URL=config.get("PICODE_API","API_URL")


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pincode', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **options):
        pincode=options.get("pincode")
        pincode_resp = reqq.get(url=PIN_CODE_API_URL+"/{}".format(pincode))
        python_dict= pincode_resp.json()
        count=0
        for i in python_dict:
            if i.get("Status")=="Success":
                postOffice_list=i.get("PostOffice")
                for j in postOffice_list:
                    count=count+1
                    default="description"
                    Name=j.get("Name")
                    Description=j.get("Description",default)
                    BranchType=j.get("BranchType")
                    DeliveryStatus=j.get("DeliveryStatus")
                    Circle=j.get("Circle")
                    District=j.get("District")
                    Division=j.get("Division")
                    Region=j.get("Region")
                    Block=j.get("Block")
                    State=j.get("State")
                    Country=j.get("Country")
                    Pincode=j.get("Pincode")
                    Mahapindata(Name=Name,Description="this is description",BranchType=BranchType,DeliveryStatus=DeliveryStatus,
                               Circle=Circle,District=District,Division=Division,Region=Region,Block=Block,
                                State=State,Country=Country,Pincode=Pincode).save()
                    self.stdout.write("DAta saved Successfully>>>>{}".format(count))

            else:
                self.stdout.write("Invalid pin number")







