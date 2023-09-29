from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
  current_page_name = 'Home'
  context = {
    'current_page_name': current_page_name
  }
  return render(request, 'dashboard/home.html', context)

@login_required
def settings_view(request):
  current_page_name = 'Settings'
  context = {
    'current_page_name': current_page_name
  }
  return render(request, 'dashboard/settings.html', context)