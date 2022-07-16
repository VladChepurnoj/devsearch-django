from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': "Ecommerce website",
        'description': 'Fully func site'
    },
    {
        'id': '2',
        'title': "Portfolio website",
        'description': 'Fully func Portfolio site'
    },
    {
        'id': '3',
        'title': "Social network",
        'description': 'Facebook clone'
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request, 'projects/single-project.html', {'project': projectObj})
