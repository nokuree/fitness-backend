from rest_framework import generics
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutList(generics.ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
