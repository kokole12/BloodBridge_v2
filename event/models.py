from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=2000)
    location = models.CharField(max_length=100)
    event_date = models.DateField('Date of the event')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("events-list")
