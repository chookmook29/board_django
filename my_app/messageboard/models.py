from django.db import models

class Message(models.Model):
	text = models.CharField(max_length=150)
	author = models.CharField(max_length=20)
