from django.shortcuts import render,  redirect
from django.db.models import Q
from django.contrib import messages
from .models import Incident
from .forms import ReportForm
from people.models import Person
from vehicles.models import Vehicle 

def reports(request):
  search_query = request.GET.get('search_query', '')
  report_list = Incident.objects.filter(
    Q(incident_description__icontains=search_query)
  )
  current_page_name = 'Reports'
  context = {
    'report': report_list,
    'current_page_name': current_page_name,
  }
  return render(request, 'reports/reports.html', context)


def add_report(request):
  if request.method == 'POST':
    form = ReportForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('reports')
  else:
    form = ReportForm()

  # Get lists of existing Persons and Vehicles
  existing_persons = Person.objects.all()
  existing_vehicles = Vehicle.objects.all()

  context = {
    'form': form,
    'existing_persons': existing_persons,
    'existing_vehicles': existing_vehicles,
  }

  return render(request, 'reports/add_report.html', context)
