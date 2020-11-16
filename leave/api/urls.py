from django.urls import path, include
from django.conf.urls import url
from . import views 


urlpatterns = [
    url('apply-leave/',views.apply_leave, name='apply' ),
    url(r'leave/applications/$',views.all_leave_applications , name='leave_applications' ),
    url(r'single-leave/applications/(\d+)/$',views.single_leave_application, name='single_leave_application' ),
    url(r'approve-leave/(\d+)/$',views.approve_leave, name='approve_leave'),
    url(r'delete-leave/(\d+)/$',views.delete_leave_application, name='delete-leave')
]