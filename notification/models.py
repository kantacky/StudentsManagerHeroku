from django.db import models

# Create your models here.

from datetime import datetime
from django.contrib.auth import get_user_model

class Category(models.Model):
    category = models.CharField(max_length = 16)

    class Meta:
        ordering = ['category']
    
    def __str__(self):
        return self.category

class Notification(models.Model):
    notifier = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    title = models.CharField(max_length = 64)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    text = models.TextField(blank = True)
    posted_datetime = models.DateTimeField(default = datetime.now)

    class Meta:
        ordering = ['-posted_datetime']
    
    def __str__(self):
        return self.title
