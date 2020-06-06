from django.shortcuts import render
from projects.models import Projects
from django.http import Http404

# Create your views here.
def project_index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    try:
        project = Projects.objects.get(pk=pk)
    except project.DoesNotExist:
        raise Http404("Question does not exist")
    
    context = {
        'project' : project
    }
    return render(request, 'project_detail.html', context)

