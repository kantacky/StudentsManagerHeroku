from django import forms
from .models import *

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['date', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'remarks']

class DeadlineForm(forms.ModelForm):
    class Meta:
        model = Deadline
        fields = ['title', 'date']