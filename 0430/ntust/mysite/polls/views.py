from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from .models import Message
from . import models

# Create your views here.
def index(request):
	m = Message.objects.all()
	return render_to_response('html/mother.html',locals())

def save(request):
	username = request.POST.get("username")
	title = request.POST.get("title")
	content = request.POST.get("content")
	message = models.Message(title=title, content=content, username=username)
	message.save()
	return HttpResponseRedirect('/polls/')