from rest_framework import generics, permissions
from .models import Workout
from .serializers import WorkoutSerializer, UserSerializer
from django.contrib.auth.models import User

def get_queryset(self):
    return Workout.objects.filter(user=self.request.user)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer