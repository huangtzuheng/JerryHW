from django.shortcuts import render_to_response

# Create your views here.
from .models import Person

def index(request):
	person = Person.objects.all()
	return render_to_response('austin/haha.html',locals())