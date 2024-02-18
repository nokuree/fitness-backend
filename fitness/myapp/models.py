from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    day = models.CharField(max_length=100)
    workouts = JSONField(default=list)  # List of workout objects

    def __str__(self):
        return f"{self.day} - Workouts: {len(self.workouts)}"
