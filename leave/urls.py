from django.urls import path, include
from django.conf.urls import url
from .views import Leaves


urlpatterns = [
    url('apply-leave/', Leaves.apply_leave, name='apply' ),
    url(r'leave/applications/$', Leaves.all_leave_applications , name='leave_applications' ),
    url(r'single-leave/applications/(\d+)/$', Leaves.single_leave_application, name='single_leave_application' ),
    url(r'approve-leave/(\d+)/$', Leaves.approve_leave, name='approve_leave'),
    url(r'delete-leave/(\d+)/$', Leaves.delete_leave_application, name='delete-leave')
]