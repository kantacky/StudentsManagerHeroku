from django.db import models

# Create your models here.

import datetime

class Message(models.Model):
    date = models.DateTimeField(auto_now = True)
    message = models.TextField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.message

class Special(models.Model):
    date = models.DateTimeField(default = datetime.datetime.now)
    title = models.CharField(max_length = 64)
    url = models.CharField(max_length = 1024)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class Info(models.Model):
    title = models.CharField(max_length = 64)
    text = models.TextField(blank = True)
    posted_datetime = models.DateTimeField(default = datetime.datetime.now)

    class Meta:
        ordering = ['-posted_datetime']
    
    def __str__(self):
        return self.title