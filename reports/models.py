from django.db import models
from django.utils import timezone

class Incident(models.Model):
  person = models.ForeignKey('people.Person', on_delete=models.SET_NULL, null=True, blank=True)
  vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.SET_NULL, null=True, blank=True)
  offence = models.ForeignKey('offences.Offence', on_delete=models.SET_NULL, null=True, blank=True)
  incident_date = models.DateTimeField()
  incident_description = models.TextField()

  def __str__(self):
    formatted_date = timezone.localtime(self.incident_date).strftime("%Y-%m-%d")
    return f"Person: {self.person} || Offence: {self.offence} || Date: {formatted_date}"