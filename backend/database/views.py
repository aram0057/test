# views.py
from django.shortcuts import render
from .models import Centre, Waste, MelbourneSuburbs

def display_data(request):
    centres = Centre.objects.select_related('waste').all()  # Fetch all centres and related waste type
    return render(request, 'centres_template.html', {'centres': centres})

# Create your views here.
