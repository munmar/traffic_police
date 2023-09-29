from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
  first_name = forms.CharField(label="First Name", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(label="Last Name", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  driving_licence_number = forms.CharField(label="Driving Licence Number", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
  address1 = forms.CharField(label="Address Line 1", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))
  city = forms.CharField(label="City", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))
  post_code = forms.CharField(label="Postal Code", max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = Person
    fields = ['first_name', 'last_name', 'driving_licence_number', 'address1', 'city', 'post_code']