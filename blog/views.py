from django.shortcuts import render
from django.http import HttpResponse, Http404
from  blog.models import Post
from django.template import RequestContext, loader
from django.template.defaultfilters import slugify
import urllib2 #to convert url to title string
import pdb; 
# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list, 'navbar': generate_navbar()}
    return render(request, 'blog/index.djhtml', context)


def view_post(request, post_name):

    #original method of unslugifying alone will fail if any symbols like commas and colons
    #are in title, 

    try:
#        post_name =  post_name.encode('ascii','ignore') #un-unicode name
      
        unslugified_post_name = post_name.replace('-', ' ')  #will get slugified name, replace all hyphens with spaces
        post = Post.objects.filter(title_text__iexact=unslugified_post_name) #set to lower first


    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'blog/posts.djhtml', {'post': post})
    

def generate_navbar():
    html = """<div id=\"nav\" class=\"u-pull-right\">
    <ul>
	  <li><a href=\"/blog/\">Home</a></li>
	  <li><a href=\"/blog/about\">About</a></li>
	  <li><a href=\"/blog/\">Blog</a></li>
	  <li><a href=\"/blog/contact\">Contact</a></li>"""
    return html
