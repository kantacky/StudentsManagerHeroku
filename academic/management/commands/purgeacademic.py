from django.core.management.base import BaseCommand, CommandError
from datetime import date, timedelta
from academic.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        Timetable.objects.filter(date = date.today() - timedelta(days = 0)).delete()
        Exam.objects.filter(start_date = date.today() - timedelta(days = 7)).delete()
        Deadline.objects.filter(date = date.today() - timedelta(days = 0)).delete()
        self.stdout.write('Deleted and Sended')