from django.urls import path
from . import views

urlpatterns = [
    
    path('filter/', views.filter_locations, name='filter_locations'),
    path('postcode/', views.list_postcodes, name='list_postcodes'),
]
