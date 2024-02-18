from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    day = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day} - {self.workout_type} (Completed: {self.is_completed})"


