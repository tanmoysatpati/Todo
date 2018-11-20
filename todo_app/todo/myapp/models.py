from django.db import models
from django.utils import timezone
from django.urls import reverse
import csv
from django.http import HttpResponse
# Create your models here.



import datetime
PRIORITY_CHOICES = (
  (1, 'In Progress'),
  (2, 'Complete'),
  (3, 'Pending'),
)
class Item(models.Model):
  title = models.CharField(max_length=250)
  description = models.TextField()
  created_date = models.DateTimeField(default=datetime.datetime.now)
  todo_task_date = models.DateTimeField(default=datetime.datetime.now)
  modified_date = models.DateTimeField(default=datetime.datetime.now)
  priority = models.IntegerField(choices=PRIORITY_CHOICES)
 

  def __str__(self):
    return self.title
