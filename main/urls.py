from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('', top, name = 'top'),
    path('info/<int:info_id>', infoDetail, name = 'infoDetail'),
]
