from django.shortcuts import render

# Create your views here.

from .models import *
from django.contrib.auth.decorators import login_required
from academic.models import *

@login_required
def top(request):
    context = {
        'messages': Message.objects.order_by('date').all(),
        'specials': Special.objects.order_by('-date').all(),
        'timetables': Timetable.objects.order_by('date').all()[0:1],
        'deadlines': Deadline.objects.order_by('date').all(),
        'title': '',
    }

    return render(request, 'main/top.html', context)

@login_required
def infoDetail(request, notification_id):
    context = {
        'info': get_object_or_404(Info, id = info_id),
        'title': 'Info Detail',
    }
    
    return render(request, 'main/info.html', context)