from django.contrib import admin
from .models import User
from .forms import UserCreationForm



admin.site.register(User)
