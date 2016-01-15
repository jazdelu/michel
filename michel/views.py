from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def home(request):
	return render_to_response("index.html",context_instance=RequestContext(request))


def comming(request):
	return render_to_response("comming.html",context_instance=RequestContext(request))

def about(request):
	return render_to_response("about.html",context_instance=RequestContext(request))

def contact(request):
	return render_to_response("contact.html",context_instance=RequestContext(request))

def blog(request):
	return render_to_response("blog.html",context_instance=RequestContext(request))

def archive(request):
	return render_to_response("archive.html",context_instance=RequestContext(request))

def lookbook(request):
	return render_to_response("lookbook.html",context_instance=RequestContext(request))

def look(request):
	return render_to_response("look.html",context_instance=RequestContext(request))

def product(request):
	return render_to_response("product.html",context_instance=RequestContext(request))

def video(request):
	return render_to_response("video.html",context_instance=RequestContext(request))

def article(request):
	return render_to_response("article.html",context_instance=RequestContext(request))

def activity(request):
	return render_to_response("activity.html",context_instance=RequestContext(request))