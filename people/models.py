from django.db import models

# Create your models here.
class Person(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  driving_licence_number = models.CharField(max_length=16)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"