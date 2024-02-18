from rest_framework import generics
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutListCreate(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
