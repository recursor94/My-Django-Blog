from django.shortcuts import render
from django.http import HttpResponse, Http404
from  blog.models import Post
from django.template import RequestContext, loader
from django.template.defaultfilters import slugify
import urllib2 #to convert url to title string
import pdb; 
# Create your views here.

def index(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {'post_list': post_list}
    return render(request, 'blog/index.djhtml', context)


def view_post(request, post_slug):

    #original method of unslugifying alone will fail if any symbols like commas and colons
    #are in title, 

    try:
      
        post = Post.objects.get(slug=post_slug) #set to lower first


    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'blog/posts.djhtml', {'post': post})


def about(request):
    """
    View for the about page
    """
    return render(request, 'blog/index.djhtml', context)
def contact(request):
    """
    view for the contact page
    """
    return render(request, 'blog/index.djhtml', context)
