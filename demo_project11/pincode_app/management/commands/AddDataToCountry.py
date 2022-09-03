from django.core.management.base import BaseCommand
from pincode_app.models import CountryMaster


class Command(BaseCommand):
    help = "This is time save data commands"
    def handle(self, *args, **options):
        CountryMaster(country_name="Paris",country_code="PR").save()
        self.stdout.write("Country saved successfullt!!!!!!!!!!!!")
