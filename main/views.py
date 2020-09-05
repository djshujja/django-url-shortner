from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import *
# Create your views here.

def homeView(request):

	urls = urlModel.objects.all()
	context = {'urls':urls}

	return render(request, 'index.html', context)

def red(request, slug):

	link = urlModel.objects.get(slug=slug)
	link.clicked()
	context ={'link':link}
	# return render(request, 'url.html', context)
	# return redirect(link.url)


	return HttpResponseRedirect('http://%s'%(link.url))
