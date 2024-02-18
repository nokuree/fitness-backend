from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('workouts/', views.WorkoutList.as_view(), name='workout_list'),
    path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name='workout_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
