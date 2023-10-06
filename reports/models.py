from django.db import models
from offences.models import Offence

class Incident(models.Model):
  person = models.ForeignKey('people.Person', on_delete=models.SET_NULL, null=True, blank=True)
  vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.SET_NULL, null=True, blank=True)
  offence = models.ForeignKey(Offence, on_delete=models.SET_NULL, null=True, blank=True)
  incident_date = models.DateTimeField()
  incident_description = models.TextField()

  def __str__(self):
    return f"{self.person} {self.offence} {self.incident_date}"