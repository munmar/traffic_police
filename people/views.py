from django.db.models import Q
from django.shortcuts import render
from .models import Person
from .forms import PersonSearchForm

# Create your views here.
# def search_people(request):
#   if request.method == 'GET':
#     form = PersonSearchForm(request.GET)
#     if form.is_valid():
#       search_query = form.cleaned_data.get('search_query')
#       people = Person.objects.filter(
#         Q(first_name__icontains=search_query) |
#         Q(last_name__icontains=search_query) |
#         Q(driving_licence_number__icontains=search_query)
#       )
#       return render(request, )
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
  return render(request, 'people.html', context)