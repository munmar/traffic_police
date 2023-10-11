from django.db import models
from auditlog.registry import auditlog

class Person(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  driving_licence_number = models.CharField(max_length=16)
  address1 = models.CharField('Address Line 1', max_length=1024)
  city = models.CharField('City', max_length=1024)
  post_code = models.CharField('Postal Code', max_length=7)

  def __str__(self):
    return f"{self.driving_licence_number} - {self.first_name} {self.last_name}"

auditlog.register(Person)