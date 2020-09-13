from django.shortcuts import render

# Create your views here.

from .models import *
from django.contrib.auth.decorators import login_required
from academic.models import *
from notification.models import *

@login_required
def top(request):
    context = {
        'messages': Message.objects.order_by('date').all(),
        'specials': Special.objects.order_by('-date').all(),
        'timetables': Timetable.objects.order_by('date').all()[0:1],
        'deadlines': Deadline.objects.order_by('date').all(),
        'notifications': Notification.objects.order_by('-posted_datetime').all()[0:5],
        'title': '',
    }

    return render(request, 'main/top/index.html', context)