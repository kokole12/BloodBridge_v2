from django.db import models
from django.urls import reverse

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.BigIntegerField()

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse("hospital-details", kwargs={"pk": self.pk})
