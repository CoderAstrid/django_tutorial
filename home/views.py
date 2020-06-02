from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def error(request):
    #return HttpResponseNotFound('<h1>not found</h1>')
    raise Http404("Not Found")

def contact(request):
    return HttpResponse("Contact us")

def about(request):
    return HttpResponse('about')
    