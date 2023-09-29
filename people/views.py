from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Person
from .forms import PersonForm

def people(request):
  search_query = request.GET.get('search_query', '')
  people_list = Person.objects.filter(
    Q(first_name__icontains=search_query) |
    Q(last_name__icontains=search_query) |
    Q(driving_licence_number__icontains=search_query)
  )
  current_page_name = 'People'
  context = {
    'people': people_list,
    'current_page_name': current_page_name,
  }
  return render(request, 'people/people.html', context)

def add_person(request):
  if request.method == 'POST':
    form = PersonForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, ("New person added to database!"))
      return redirect('people')
  else:
    form = PersonForm()
  
  return render(request, 'people/add_person.html', {'form': form})