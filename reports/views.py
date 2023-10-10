from django.shortcuts import render,  redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Incident
from .forms import ReportForm
from people.models import Person
from vehicles.models import Vehicle 

def reports(request):
  search_query = request.GET.get('search_query', '')
  report_list = Incident.objects.select_related('person').filter(
    Q(incident_description__icontains=search_query) |
    Q(person__first_name__icontains=search_query) |
    Q(person__last_name__icontains=search_query)
  )
  current_page_name = 'Reports'
  context = {
    'reports': report_list,
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

def edit_report(request, report_id):
  report = get_object_or_404(Incident, pk=report_id)

  if request.method == 'POST':
    form = ReportForm(request.POST, instance=report)
    if form.is_valid():
      form.save()
      return redirect('reports')
  else:
    form = ReportForm(instance=report)

  return render(request, 'reports/edit_report.html', {'report': report, 'form': form})