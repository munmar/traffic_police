from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.dashboard, name='home'),
  path('settings/', views.settings_view, name='settings'),
]