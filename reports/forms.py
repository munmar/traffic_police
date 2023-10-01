from django import forms
from .models import Incident
from people.models import Person
from vehicles.models import Vehicle

class ReportForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['description', 'person', 'vehicle']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.all()
        self.fields['vehicle'].queryset = Vehicle.objects.all()
