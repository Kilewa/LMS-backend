from django.urls import path
from profiles.api.views import ProfileApi, ProfileDetailApi

app_name = 'profiles'

urlpatterns = [
    path('profile/', ProfileApi.as_view()),
    path('profile/<int:pk>/', ProfileDetailApi.as_view()),
]