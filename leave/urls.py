from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('apply-leave/', views.apply_leave, name='apply' ),
    url('leave/applications/', views.all_leave_applications , name='leave_applications' ),
    url(r'single-leave/applications/(\d+)', views.single_leave_application, name='single_leave_application' ),
]