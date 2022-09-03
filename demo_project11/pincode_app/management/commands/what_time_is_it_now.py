from django.core.management.base import BaseCommand
import datetime
import time
from django.utils import timezone

class Command(BaseCommand):
    help = "This is time commands"
    def handle(self, *args, **options):
        dt = datetime.datetime.now()
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
