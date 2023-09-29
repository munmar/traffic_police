from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
  registration = forms.CharField(label="Registration", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  make = forms.CharField(label="Make", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  model = forms.CharField(label="Model", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
  colour = forms.CharField(label="Colour", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  class Meta:
    model = Vehicle
    fields = ['registration', 'make', 'model', 'colour']