from django.shortcuts import render
from .models import Message

def home(request):
	all_messages = Message.objects.all
	return render(request, 'index.html', {'all_messages': all_messages})

def about(request):
	return render(request, 'about.html', {})