from django import forms

class PersonSearchForm(forms.Form):
  search_query = forms.CharField(max_length=255, required=False)