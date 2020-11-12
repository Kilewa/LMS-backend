from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url('all-tasks/', views.all_tasks, name="all_tasks"),
    url(r'single-task/(\d+)', views.single_task, name="single_task")
]