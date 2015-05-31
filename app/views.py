from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers
from datetime import datetime
from models.book import book
from models.user import user
from parameter import parameter
from PIL import ImageFile
import time
import hashlib

def index(request):
    assert isinstance(request, HttpRequest)
    b=book()
    try:
    	u=request.COOKIES["username"]
    except Exception as err:
    	u=False
    return render(request,
        'content/index.html',
        context_instance = RequestContext(request,
        {
            'books':b.select(1 if parameter.getParameter(request,"page")==0 else parameter.getParameter(request,"page"),30),
        	'username' :u
        }))
def context(request):
	assert isinstance(request,HttpRequest)
	b=book()
	try:
		u=request.COOKIES["username"]
	except Exception as err:
		u=False
	return render(request,
		'content/context.html',
		context_instance = RequestContext(request,
		{
			'book':b.find(parameter.getParameter(request,"id")),
			'next_book':b.findNext(parameter.getParameter(request,"id")),
			'previous_book':b.findPrevious(parameter.getParameter(request,"id")),
			'username' :u
		}))
def login(request):
	assert isinstance(request,HttpRequest)
	u=user()
	username=request.REQUEST.get('username','')
	password=request.REQUEST.get('password','')
	if u.login(username,password):
		res='{"status":1,"message":"success","username":"'+username+'"}'
		response=HttpResponse(res,content_type="application/json")
		response.set_cookie('username',username, 3000000)
	else:
		res='{"status":0,"message":"error"}'
		response=HttpResponse(res,content_type="application/json")
	return response 
def register(request):
	assert isinstance(request,HttpRequest)
	u=user()
	username=request.REQUEST.get('username','')
	password=request.REQUEST.get('password','')
	status=u.register(username,password)
	if status==True:
		res=res='{"status":0,"message":"success","username":"'+username+'"}'
		response=HttpResponse(res,content_type="application/json")
		response.set_cookie('username',username, 3000000)
	else:
		res='{"status":'+str(status)+',"message":"error"}'
		response=HttpResponse(res,content_type="application/json")
	return response 
def share(request):
	assert isinstance(request,HttpRequest)
	b=book()
	try:
		u=request.COOKIES["username"]
	except Exception as err:
		u=False
	return render(request,
		'content/share.html',
		context_instance = RequestContext(request,
		{
			'username' :u
		}))
def update(request):
	assert isinstance(request,HttpRequest)
	try:
		f = request.FILES["image"]  
		parser = ImageFile.Parser()  
		for chunk in f.chunks():  
			parser.feed(chunk)  
			img = parser.close()
			m=hashlib.md5()
			m.update(str(time.time()))
			img.save("app/static/updata/images/"+m.hexdigest()+".jpg") 
		return HttpResponse('{"status":1,"file":"'+"app/static/updata/images/"+m.hexdigest()+".jpg"+'"}');
	except Exception as err:
		return HttpResponse('{"status":0}');
def updateIn(request):
	assert isinstance(request,HttpRequest)
	b=book()
	u=user()
	title=request.REQUEST.get('title','')
	image=request.REQUEST.get('image','')
	author=request.REQUEST.get('author','')
	introduction=request.REQUEST.get('introduction','')
	recommend=request.REQUEST.get('recommend','')
	line=request.REQUEST.get('line','')
	t=time.strftime('%Y-%m-%d',time.localtime(time.time()))
	username=u.getUsername(request.COOKIES["username"])
	try:
		if b.add(title,image,author,introduction,recommend,line,t,username):
			return HttpResponse('{"status":1}')
		else:
			return HttpResponse('{"status":0}');
	except Exception as err:
		return HttpResponse('{"status":0}');