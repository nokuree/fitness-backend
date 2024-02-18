from django.urls import path
from .views import WorkoutList

urlpatterns = [
    path('api/workouts/', WorkoutList.as_view(), name='workouts'),
]
