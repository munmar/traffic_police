from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PasswordChangingForm, CreateUserForm
from django.contrib.auth.models import User
from auditlog.models import LogEntry
from django.db.models import Q
import json


# Create your views here.
def login_user(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      # Redirect to a success page.
      return redirect('home')
    else:
      messages.success(request, ("There was an error logging in. Please try again..."))
      return redirect('login')
  else:
    return render(request, 'authentication/login.html', {})

def logout_user(request):
  logout(request)
  messages.success(request, ("You have successfully logged out!"))
  return redirect('login')

class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangingForm
  # form_class = PasswordChangeForm
  success_url = reverse_lazy('change-password')

  def form_valid(self, form):
    messages.success(self.request, "Your password has been changed successfully.")
    return super().form_valid(form)
  
def manage(request):
  search_query = request.GET.get('search_query', '')
  user_list = User.objects.filter(
    Q(username__icontains=search_query) |
    Q(password__icontains=search_query) |
    Q(is_superuser__icontains=search_query)
  )
  current_page_name = 'Manage Users'
  context = {
    'users': user_list,
    'current_page_name': current_page_name,
  }
  return render(request, 'management/manage.html', context)

User = get_user_model()
def add_user(request):
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_superuser = form.cleaned_data['is_superuser']
      user.save()
      return redirect('manage')
  else:
    form = CreateUserForm()
  
  context = {
    'form': form,
  }
  
  return render(request, 'management/add_user.html', context)

def delete_user(request, user_id):
  user = get_object_or_404(User, id=user_id)
  user.delete()
  return redirect('manage')

# def audit_log(request):
#   audit_entries = LogEntry.objects.all().order_by('-timestamp')
#   parsed_entries = []
#   for entry in audit_entries:
#     changes = json.loads(entry.changes)
#     for table_modified, change_list in changes.items():
#       parsed_entries.append({
#         'table_modified': table_modified,
#         'changes': ', '.join(change_list),
#         'timestamp': entry.timestamp,
#         'actor': entry.actor,
#         'action': entry.action,
#         'record_id': entry.object_id,
#       })
#   current_page_name = 'Audit Log'
#   context = {
#     'audit_entries': parsed_entries,
#     'current_page_name': current_page_name  
#   }
#   return render(request, 'audit/auditlog.html', context)

def audit_log(request):
  audit_entries = LogEntry.objects.all().order_by('-timestamp')  # Retrieve audit entries

  parsed_entries = []
  for entry in audit_entries:
    changes = json.loads(entry.changes)  # Deserialize the JSON string
    for table_modified, change_list in changes.items():
      old_value, new_value = change_list
      formatted_change = f"FROM: {old_value} -> TO: {new_value}"
      parsed_entries.append({
        'old_value': old_value,
        'new_value': new_value,
        'table_modified': table_modified,
        'changes': formatted_change,
        'timestamp': entry.timestamp,
        'actor': entry.actor,
        'action': entry.action,
        'record_id': entry.object_id,
      })

  current_page_name = 'Audit Log'
  context = {
    'audit_entries': parsed_entries,
    'current_page_name': current_page_name  
  }
  return render(request, 'audit/auditlog.html', context)