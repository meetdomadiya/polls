from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #this is a simplest view possible in django. to call this view we need to configure url
    return HttpResponse("Hello world! You are at polls index!")

def about(request):
    #this is a simplest view possible in django. to call this view we need to configure url
    return HttpResponse("Hello world! My name is Meet!")
