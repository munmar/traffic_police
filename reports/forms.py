from django import forms
from .models import Incident
from people.models import Person
from vehicles.models import Vehicle
from offences.models import Offence

class ReportForm(forms.ModelForm):
    person = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        label="Person",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(),
        label="Vehicle",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    offence = forms.ModelChoiceField(
        queryset=Offence.objects.all(),
        label="Offence",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    incident_date = forms.DateTimeField(label="Incident Date", widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    incident_description = forms.CharField(label="Incident Description", max_length=1024, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Incident
        fields = ['person', 'vehicle', 'offence', 'incident_date', 'incident_description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.all()
        self.fields['vehicle'].queryset = Vehicle.objects.all()
