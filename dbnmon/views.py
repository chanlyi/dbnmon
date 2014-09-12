# Create your views here.
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
#from dbnmon.models import BlogsPost

def dbnmon(request):
	#posts = BlogsPost.objects.all()
	t = loader.get_template("index.html")
	c = Context({})
	return HttpResponse(t.render(c))


