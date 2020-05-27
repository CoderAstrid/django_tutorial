from django.shortcuts import render
from django.http import HttpResponse # added by astrid
from .models import *
from .forms import FeedbackForm
# Create your views here.

#added by astrid
def index(request):
    msg = 'My Message'
    return render(request, 'home/index.html', {'message': msg})
    # return HttpResponse("Hello, World!")

def create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})