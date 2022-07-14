from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})