from django.shortcuts import render
from django.http import HttpResponse # added by astrid
# Create your views here.

#added by astrid
def index(request):
    msg = 'My Message'
    return render(request, 'home/index.html', {'message': msg})
    # return HttpResponse("Hello, World!")