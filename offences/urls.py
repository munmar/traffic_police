from django.urls import path
from . import views

urlpatterns = [
  path('fines/', views.add_fine, name='add_fine'),
]