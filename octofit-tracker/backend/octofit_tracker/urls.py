"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('teams/', views.TeamViewSet.as_view({'get': 'list'}), name='team-list'),
    path('activities/', views.ActivityViewSet.as_view({'get': 'list'}), name='activity-list'),
    path('leaderboard/', views.LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard-list'),
    path('workouts/', views.WorkoutViewSet.as_view({'get': 'list'}), name='workout-list'),
]
