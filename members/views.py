from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PasswordChangingForm

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