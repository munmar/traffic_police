from django.urls import path
from . import views

urlpatterns = [
  path('reports/', views.reports, name='reports'),
  path('reports/add/', views.add_report, name='add_report'),
  # path('reports/view/', views.view_report, name='view_report')
]