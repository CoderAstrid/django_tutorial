from django.shortcuts import render
from django.http import HttpResponse # added by astrid
# Create your views here.

#added by astrid
def index(request):
    return HttpResponse("Hello, World!")