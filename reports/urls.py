from django.urls import path
from . import views

urlpatterns = [
  path('reports/', views.reports, name='reports'),
  path('reports/add/', views.add_report, name='add_report'),
  path('reports/edit-report/<int:report_id>/', views.edit_report, name='edit_report'),
]