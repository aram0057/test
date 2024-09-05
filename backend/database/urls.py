# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('centres/', views.display_data, name='display_centres'),
]
