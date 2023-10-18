from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from people.models import Person
from vehicles.models import Vehicle
from reports.models import Incident

# Home page view
@login_required
def dashboard(request):
  current_page_name = 'Home'
  person_count = Person.objects.count()
  vehicle_count = Vehicle.objects.count()
  report_count = Incident.objects.count()

  context = {
    'current_page_name': current_page_name,
    'person_count': person_count,
    'vehicle_count': vehicle_count,
    'report_count': report_count,
  }
  return render(request, 'dashboard/home.html', context)

# Settings view
@login_required
def settings_view(request):
  current_page_name = 'Settings'
  context = {
    'current_page_name': current_page_name
  }
  return render(request, 'dashboard/settings.html', context)