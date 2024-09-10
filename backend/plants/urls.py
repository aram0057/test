from django.urls import path
from .views import plant_recommendation,plant_full_list,compost_calculator,compost_guide,test_page

urlpatterns = [
    path('recommend/', plant_recommendation, name='recommend_plant'),  # Use the view directly
    path('full-list/',plant_full_list,name = 'plant_full_list' ),
    path('compost-calculator/', compost_calculator, name='compost_calculator'),
    path('compost-guide/', compost_guide, name='compost_guide'),
    path('test/', test_page, name='test_page'),
]
