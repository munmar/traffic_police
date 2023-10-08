from django import forms
from .models import Fine
from reports.models import Incident

class FineForm(forms.ModelForm):
  fine_amount = forms.DecimalField(label="Fine", min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
  fine_points = forms.IntegerField(label="Points", min_value=0, max_value=12, step_size=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
  incident = forms.ModelChoiceField(
        queryset=Incident.objects.all(),
        label="Incident",
        empty_label="Select an incident",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    # incidents that do not have associated fines
    incidents_without_fines = Incident.objects.exclude(fine__isnull=False)
    
    # choices for the 'incident' field w/o fines
    self.fields['incident'].queryset = incidents_without_fines

  class Meta:
    model = Fine
    fields = ['fine_amount', 'fine_points', 'incident']