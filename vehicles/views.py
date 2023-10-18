from django.shortcuts import render,  redirect
from django.db.models import Q
from django.contrib import messages
from .models import Vehicle
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required

# Vehicle view
@login_required
def vehicles(request):
  search_query = request.GET.get('search_query', '')
  vehicle_list = Vehicle.objects.filter(
    Q(registration__icontains=search_query)
  )
  current_page_name = 'Vehicles'
  context = {
    'vehicles': vehicle_list,
    'current_page_name': current_page_name,
  }
  return render(request, 'vehicles/vehicles.html', context)

# Adding a new vehicle
@login_required
def add_vehicle(request):
  current_page_name = 'Add New Vehicle'
  if request.method == 'POST':
    form = VehicleForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, ("New vehicle added to database!"))
      return redirect('vehicles')
  else:
    form = VehicleForm()
  
  context = {
    'current_page_name': current_page_name,
    'form': form,
  }

  return render(request, 'vehicles/add_vehicle.html', context)