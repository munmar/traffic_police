from django import forms
from .models import Incident
from people.models import Person
from vehicles.models import Vehicle
from offences.models import Offence

class ReportForm(forms.ModelForm):
    person = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        label="Person",
        empty_label="Select a person",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(),
        label="Vehicle",
        empty_label="Select a vehicle",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    offence = forms.ModelChoiceField(
        queryset=Offence.objects.all(),
        label="Offence",
        empty_label="Select an offence",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    incident_date = forms.DateTimeField(label="Incident Date", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    incident_description = forms.CharField(label="Incident Description", max_length=1024, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter incident description'}))

    class Meta:
        model = Incident
        fields = ['person', 'vehicle', 'offence', 'incident_date', 'incident_description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.all()
        self.fields['vehicle'].queryset = Vehicle.objects.all()
