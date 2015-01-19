from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world, you're at a test page.")

def view_post(request, post_id):
    return HttpResponse("This is post %s." % post_id)
