from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Message

def home(request):
	all_messages = Message.objects.all
	return render(request, 'index.html', {'all_messages': all_messages})


def login_user(request):
	return render(request, 'login.html', {})


def about(request):
	return render(request, 'about.html', {})