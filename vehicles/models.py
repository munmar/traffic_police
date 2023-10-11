from django.db import models
from auditlog.registry import auditlog

class Vehicle(models.Model):
  registration = models.CharField(max_length=7)
  make = models.CharField(max_length=255)
  model = models.CharField(max_length=255)
  colour = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.registration}"

auditlog.register(Vehicle)