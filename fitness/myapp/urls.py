from django.urls import path
from .views import WorkoutListCreate

urlpatterns = [
    path('api/workouts/', WorkoutListCreate.as_view(), name='workout-list'),
]
