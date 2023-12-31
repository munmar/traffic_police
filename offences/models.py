from django.db import models
from auditlog.registry import auditlog

class Offence(models.Model):
  offence_description = models.TextField()
  offence_max_fine = models.DecimalField(max_digits=10, decimal_places=2)
  offence_max_points = models.PositiveIntegerField()

  def __str__(self):
    return self.offence_description


class Fine(models.Model):
  fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
  fine_points = models.PositiveIntegerField()
  incident = models.ForeignKey('reports.Incident', on_delete=models.CASCADE)

  def __str__(self):
    return f"Fine for Incident ID: {self.incident}"

auditlog.register(Fine)