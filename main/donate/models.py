from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Appointment(models.Model):
    reason = models.CharField(default="donate blood",max_length=100)
    contact = models.CharField(max_length=20)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reason

    def get_absolute_url(self):
        return reverse("appointment-detail", kwargs={"pk": self.pk})
