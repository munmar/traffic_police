from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'dashboard/home.html', {})

@login_required
def settings_view(request):
  return render(request, 'dashboard/settings.html', {})

@login_required
def change_password(request):
  return render(request, 'dashboard/settings/change_password.html', {})