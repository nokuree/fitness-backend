# Inside your Django app's views.py file

from django.http import JsonResponse
from .models import Workout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

@require_POST
@login_required
def add_workout(request):
    try:
        data = json.loads(request.body)
        # Assuming 'data' contains 'day', 'workouts' (list of workout objects)
        workout_instance = Workout.objects.create(
            user=request.user,
            day=data['day'],
            workouts=data['workouts']
        )
        return JsonResponse({'status': 'success', 'workout': workout_instance.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optionally log the user in immediately after registration
            return redirect('home')  # Redirect to a home page or another appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})