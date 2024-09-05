from django.shortcuts import render
from .models import Centre, Waste, MelbourneSuburbs
import json


def filter_locations(request):
    # Get the selected waste type from the dropdown
    waste_type = request.GET.get('waste_type', None)
    
    # Fetch the waste types dynamically
    waste_types = Waste.objects.values_list('waste_type', flat=True).distinct()

    if waste_type:
        try:
            # Get the waste type and corresponding centers
            waste = Waste.objects.get(waste_type=waste_type)
            centres = Centre.objects.filter(waste=waste)
        except Waste.DoesNotExist:
            centres = Centre.objects.none()
    else:
        centres = Centre.objects.all()  # Return all centers if no filter

    # Prepare the data for rendering (convert Decimal fields to float)
    centres_data = list(centres.values('name', 'address', 'latitude', 'longitude', 'waste__waste_type'))
    for centre in centres_data:
        centre['latitude'] = float(centre['latitude'])
        centre['longitude'] = float(centre['longitude'])

    # Send data to template
    context = {
        'centres': centres,
        'centres_data_json': json.dumps(centres_data),  # Convert to JSON for use in JavaScript
        'waste_types': waste_types # Pass available waste types to the template
        
    }
    return render(request, 'centres_template.html', context)


def list_postcodes(request):
    # Fetch all records from the MelbourneSuburbs model
    suburbs = MelbourneSuburbs.objects.all()
    # Pass the data to the template
    return render(request, 'centres_template.html', {'suburbs': suburbs})