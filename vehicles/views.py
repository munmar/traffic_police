from django.shortcuts import render,  redirect
from django.db.models import Q
from django.contrib import messages
from .models import Vehicle
from .forms import VehicleForm

def vehicles(request):
  search_query = request.GET.get('search_query', '')
  vehicle_list = Vehicle.objects.filter(
    Q(registration__icontains=search_query)
  )
  current_page_name = 'Vehicles'
  context = {
    'vehicle': vehicle_list,
    'current_page_name': current_page_name,
  }
  return render(request, 'vehicles/vehicles.html', context)

def add_vehicle(request):
  if request.method == 'POST':
    form = VehicleForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, ("New vehicle added to database!"))
      return redirect('vehicles')
  else:
    form = VehicleForm()
  
  return render(request, 'vehicles/add_vehicle.html', {'form': form})