# Inside your Django app's urls.py file

from django.urls import path
from .views import add_workout
from .views import register

urlpatterns = [
    path('api/workouts/add/', add_workout, name='add_workout'),
    path('register/', register, name='register'),
    # Other URL patterns...
]
