from django.urls import path
from . import views

urlpatterns = [
  path('vehicles/', views.vehicles, name='vehicles'),
  path('vehicles/add/', views.add_vehicle, name='add_vehicle'),
]