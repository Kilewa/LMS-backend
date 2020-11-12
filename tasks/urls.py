from django.urls import path, include
from . import views

urlpatterns = [
    path('all-tasks/', views.alltasks, name="all_tasks")
]