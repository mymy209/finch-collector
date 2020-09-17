from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)


