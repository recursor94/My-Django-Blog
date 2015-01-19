from django.shortcuts import render
from django.http import HttpResponse, Http404
from  blog.models import Post
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.djhtml', context)

def view_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)

    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/posts.djhtml', {'post': post})
    
