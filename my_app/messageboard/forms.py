from django import forms
from .models import Message

class Message_form(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['text']