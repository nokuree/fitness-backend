# Inside your Django app's models.py file

from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    workouts = JSONField()  # Stores the list of workouts

    def __str__(self):
        return f"{self.day} - {self.user.username}"

