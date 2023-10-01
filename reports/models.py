from django.db import models
from people.models import Person
from vehicles.models import Vehicle
from offences.models import Offence

class Incident(models.Model):
  person_id = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
  vehicle_id = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
  offence_id = models.ForeignKey(Offence, on_delete=models.SET_NULL, null=True, blank=True)
  incident_date = models.DateTimeField()
  incident_description = models.TextField()

  def __str__(self):
    return f"{self.person_id} {self.offence_id} {self.incident_date}"