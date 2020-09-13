from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path('<int:pk>/', UserDetail.as_view(), name = 'detail'),
    path('editpasswd/', EditPasswd.as_view(), name = 'editpasswd')
]
