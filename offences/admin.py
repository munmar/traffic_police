from django.contrib import admin
from .models import Offence, Fine
# Register your models here.
admin.site.register(Offence)
admin.site.register(Fine)