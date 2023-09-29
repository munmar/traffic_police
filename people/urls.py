from django.urls import path
from . import views

urlpatterns = [
  path('people/', views.people, name='people'),
  path('people/add/', views.add_person, name='add_person'),
]