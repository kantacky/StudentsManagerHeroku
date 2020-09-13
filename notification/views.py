from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.template.loader import get_template

@login_required
def index(request):
    context = {
        'notifications': Notification.objects.order_by('-posted_datetime').all(),
        'title': 'Notification',
    }

    return render(request, 'notification/index.html', context)

@login_required
def detail(request, notification_id):
    context = {
        'notification': get_object_or_404(Notification, id = notification_id),
        'title': 'Notification Detail',
    }
    
    return render(request, 'notification/detail.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = NotificationForm(request.POST, instance = Notification())
        if form.is_valid():
            notifier = get_user_model().objects.get(id = request.user.id)
            title = request.POST.get('title')
            category_id = request.POST.get('category')
            category = Category.objects.get(pk = category_id)
            text = request.POST.get('text')
            Notification(notifier = notifier, title = title, category = category, text = text).save()

            template = get_template('push/notification.txt')
            context = {
                "notifier": notifier,
                "title": title,
                "category": category,
            }
            text = template.render(context)
            channels.send(text)

            return redirect('notification:index')
    else:   
        form = NotificationForm()
    
    context = {
        'form': NotificationForm(instance = Notification()),
        'title': 'New Notification',
    }

    return render(request, 'notification/create.html', context)