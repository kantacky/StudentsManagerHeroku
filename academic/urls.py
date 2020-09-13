from django.urls import path

from .views import *

app_name = 'academic'

urlpatterns = [
    path('timetable/', TimetableIndex, name = 'TimetableIndex'),
    path('timetable/create/', TimetableCreate, name = 'TimetableCreate'),
    path('timetable/edit/<int:timetable_id>', TimetableEdit, name = 'TimetableEdit'),
    path('exam/', ExamIndex, name = 'ExamIndex'),
    path('deadline/', DeadlineIndex, name = 'DeadlineIndex'),
    path('deadline/create/', DeadlineCreate, name = 'DeadlineCreate')
]
