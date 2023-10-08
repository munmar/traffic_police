from django.shortcuts import render, redirect
from .forms import FineForm

def add_fine(request):
  if request.method == 'POST':
    form = FineForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
  else:
    form = FineForm()

  context = {
    'form': form,
  }
  return render(request, 'fines/add_fine.html', context)