from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers
from models.admin import admin
from models.book import book

def login(request):
	assert isinstance(request, HttpRequest)
	return render(request,
        'admin/login.html',
        context_instance = RequestContext(request,
        {
            'status':True if request.REQUEST.get('error','')=="" else False
        }))
def loginIn(request):
	assert isinstance(request,HttpRequest)
	a=admin()
	username=request.REQUEST.get('username','')
	password=request.REQUEST.get('password','')
	if a.login(username,password):
		response=HttpResponseRedirect("/admin/index.html")
		response.set_cookie('admin',username)
		return response
	else:
		return HttpResponseRedirect("/admin/login.html?error=1")
def index(request):
	assert isinstance(request,HttpRequest)
	return render(request,
		'admin/index.html',
		context_instance = RequestContext(request,
		{

		}))
def getBook(request):
	assert isinstance(request,HttpRequest)
	b=book()
	return render(request,
		'admin/book.html',
		context_instance = RequestContext(request,
		{
			"books":b.select(1,30)
		}))