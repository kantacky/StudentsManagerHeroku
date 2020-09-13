from django.urls import path

from .views import *

app_name = 'notification'

urlpatterns = [
    path('', index, name = 'index'),
    path('detail/<int:notification_id>', detail, name = 'detail'),
    path('create/', create, name = 'create'),
]
