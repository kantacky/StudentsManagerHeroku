from django.db import models

# Create your models here.

import datetime

class Subject(models.Model):
    subject = models.CharField(max_length = 16)

    class Meta:
        ordering = ['subject']
    
    def __str__(self):
        return self.subject


class Timetable(models.Model):
    date = models.DateField(default = datetime.date.today)
    first = models.ForeignKey(Subject, on_delete = models.CASCADE, blank = True, null = True, related_name = 'first')
    second = models.ForeignKey(Subject, on_delete = models.CASCADE, blank = True, null = True, related_name = 'second') 
    third = models.ForeignKey(Subject, on_delete = models.CASCADE, blank = True, null = True, related_name = 'third')
    fourth = models.ForeignKey(Subject, on_delete = models.CASCADE, blank = True, null = True, related_name = 'fourth')
    fifth = models.ForeignKey(Subject, on_delete = models.CASCADE, blank = True, null = True, related_name = 'fifth')
    sixth = models.ForeignKey(Subject, on_delete = models.CASCADE, blank = True, null = True, related_name = 'sixth')
    seventh = models.ForeignKey(Subject, on_delete = models.CASCADE, blank = True, null = True, related_name = 'seventh')
    remarks = models.TextField(blank = True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return format(self.date)


class Exam(models.Model):
    title = models.CharField(max_length = 32)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.title

class Coverage(models.Model):
    title = models.ForeignKey(Exam, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    coverage = models.TextField()

class Deadline(models.Model):
    title = models.CharField(max_length = 64)
    date = models.DateField(default = datetime.date.today)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title