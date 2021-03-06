from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Message
from django.contrib import messages
from .forms import Message_form

def home(request):
	return render(request, 'index.html', {})


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main')
		else:
			messages.success(request, ('Wrong username or password'))
			return redirect('login')
	else:
		return render(request, 'login.html', {})


def about(request):
	return render(request, 'about.html', {})


def main(request):
	if request.method == 'POST':
		form = Message_form(request.POST or None)
		if form.is_valid():
			form.save()
			all_messages = Message.objects.all
			return render(request, 'main.html', {'all_messages': all_messages})
	else:
		all_messages = Message.objects.all
		return render(request, 'main.html', {'all_messages': all_messages})