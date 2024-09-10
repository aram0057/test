from django.shortcuts import render
from .models import Plant,Plant_Needs
from django.http import HttpResponse

def plant_recommendation(request):
    if request.method == 'POST':
        # Get the form data
        category = request.POST.get('category')
        sunlight_needs = request.POST.get('sunlight_needs')
        watering_needs = request.POST.get('watering_needs')

        # Filter plants based on the selected criteria
        recommended_plants = Plant.objects.filter(
            category=category,
            sunlight_needs=sunlight_needs,
            watering_needs=watering_needs
        )

        # Fetch plant needs if required
        plant_needs = Plant_Needs.objects.filter(plant__in=recommended_plants)

        return render(request, 'plants/plant_list.html', {
            'plants': recommended_plants,
            'plant_needs': plant_needs,
            'category': category,
            'sunlight_needs': sunlight_needs,
            'watering_needs': watering_needs,
        })

    # If GET request, just render the form
    return render(request, 'plants/plant_form.html')

def plant_full_list(request):
    plants = Plant.objects.all()
    return render(request, 'plants/plant_full_list.html', {'plants': plants})


def compost_calculator(request):
    if request.method == 'POST':
        try:
            greens = float(request.POST.get('greens', 0))
            browns = float(request.POST.get('browns', 0))
            
            # Check if inputs are valid
            if greens <= 0 or browns <= 0:
                raise ValueError("Invalid input")

            # Calculate ratio
            ratio = browns / greens
            recommended_ratio = 2  # Recommended ratio (browns:greens)
            balance_message = "Your compost ratio is balanced." if ratio >= recommended_ratio else "Add more browns to balance the compost ratio."

            return render(request, 'plants/compost_calculator.html', {
                'ratio': ratio,
                'balance_message': balance_message,
                'greens': greens,
                'browns': browns
            })
        except ValueError:
            return render(request, 'plants/compost_calculator.html', {
                'error': "Please enter valid numbers greater than zero."
            })

    return render(request, 'plants/compost_calculator.html')

def compost_guide(request):
    return render(request, 'plants/compost_guide.html')


def test_page(request):
    return render(request, 'plants/test_page.html')
