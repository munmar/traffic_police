from django.shortcuts import render,  redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Incident
from .forms import ReportForm
from people.models import Person
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required

# Reports view
@login_required
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

# Adding a new report
@login_required
def add_report(request):
  current_page_name = 'Add New Report'
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
    'current_page_name': current_page_name,
    'form': form,
    'existing_persons': existing_persons,
    'existing_vehicles': existing_vehicles,
  }

  return render(request, 'reports/add_report.html', context)

# Editing an existing report
@login_required
def edit_report(request, report_id):
  current_page_name = 'Add New Report'

  report = get_object_or_404(Incident, pk=report_id)

  if request.method == 'POST':
    form = ReportForm(request.POST, instance=report)
    if form.is_valid():
      form.save()
      return redirect('reports')
  else:
    form = ReportForm(instance=report)

  context = {
    'current_page_name': current_page_name, 
    'report': report, 
    'form': form,
  }

  return render(request, 'reports/edit_report.html', context)