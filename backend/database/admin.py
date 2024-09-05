from django.contrib import admin

# Register your models here.
from .models import Waste,MelbourneSuburbs

admin.site.register(Waste)
admin.site.register(MelbourneSuburbs)