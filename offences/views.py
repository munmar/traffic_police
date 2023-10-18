from django.shortcuts import render, redirect
from .forms import FineForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Adding a new fine
@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_fine(request):
  if request.method == 'POST':
    form = FineForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
  else:
    form = FineForm()
  current_page_name = 'Add Fine'
  context = {
    'form': form,
    'current_page_name': current_page_name,
  }
  return render(request, 'fines/add_fine.html', context)