from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from database import serializers
from .filters import ServiceFilter
from .models import Service
from .models import Tool
from .models import ToolType
from .models import Database
from .models import Event
from .models import Formation
from .models import Training_material
from .models import Platform


def name_service(request, id):

    a_list = Service.objects.filter(id=id)
    context = {'id': id, 'service_list': a_list}
    return render(request, 'database/name_service.html', context)

class ServiceListView(ListView):

    model = Service

    def get_queryset(self):

        return Service.objects.all()

def service_detail(request):
    return Service.objects.filter(name='Phylogeny.fr')

def service_list(request):
    f = ServiceFilter(request.GET, queryset=Service.objects.all())
    return render(request, 'database/template.html', {'filter': f})

def search(request):
    services_list = Service.objects.all()
    services_filter = ServiceFilter(request.GET, queryset=services_list)
    return render(request, 'database/services_list.html', {'filter': services_filter})

def index(request):
    return render(request, 'database/template.html')


    return HttpResponse("Welcome to the Catalogue of French resources in bioinformatics")



class ServiceViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allows users to be viewed or edited.
     """
     queryset = Service.objects.all().order_by('-name')
     serializer_class = serializers.ServiceSerializer


class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tool.objects.all().order_by('-name')
    serializer_class = serializers.ToolSerializer

class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all().order_by('-name')
    serializer_class = serializers.DatabaseSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-name')
    serializer_class = serializers.EventSerializer

class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all().order_by('-name')
    serializer_class = serializers.FormationSerializer

class Training_materialViewSet(viewsets.ModelViewSet):
    queryset = Training_material.objects.all().order_by('-name')
    serializer_class = serializers.Training_materialSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all().order_by('-name')
    serializer_class = serializers.PlatformSerializer