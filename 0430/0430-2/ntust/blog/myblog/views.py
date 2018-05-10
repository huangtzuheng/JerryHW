from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from . import models
import datetime

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	if request.method == 'POST':
		pk = request.POST.get('pk')
		Post.objects.get(pk=pk).delete()
	post_list = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_page(request):
	return render_to_response('blog/post_new.html')

def save(request):
	user = request.POST.get("tb_user")
	ti = request.POST.get("tb_title")
	tx = request.POST.get("tb_text")
	created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	n_post = models.Post(author = user, title = ti, text = tx, created_date = created, published_date = publish)
	n_post.save()

	return HttpResponseRedirect('/')

def edit_page(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.author = request.POST.get('author')
		post.title = request.POST.get('title')
		post.text = request.POST.get('text')
		post.save()
		return redirect('/')
	return render(request, 'blog/post_edit.html', {'post': post})

#def delete(request):
#	de = request.GET.get('i')    
#	post = Post.objects.get(de=de)
#	if request.method == 'POST':
#		post.author = request.POST.get('author')
#		post.title = request.POST.get('title')
#		post.text = request.POST.get('text')
#		post.delete()
#		return redirect('/')
#	return HttpResponseRedirect('/')