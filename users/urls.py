from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .api import *

urlpatterns = [
      path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
      path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
      path('api/register', RegisterApi.as_view(), name='register'),
      path('api/activate/<uidb64>/<token>',activate_account, name='activate'),
      path('api/login', UserLoginView.as_view(), name='login'),
      path('api/departmenthead', DepartmentheadView.as_view(), name='department_heads'),
      path('api/departmenthead/<int:deptid>',DepartmentheadView.as_view()),
      path('api/employee', EmployeeListView.as_view(), name='employees'),
      path('api/employee/<int:empid>',EmployeeView.as_view()),
]


