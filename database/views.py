from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import generics
import django_filters.rest_framework

from database import serializers
from .filters import ServiceFilter
from .filters import DatabaseFilter
from .filters import ToolFilter
from .models import Service
from .models import Tool
from .models import ToolType
from .models import Database
from .models import Event
from .models import Formation
from .models import Training_material
from .models import Platform
from .models import Resource
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from database.serializers import DatabaseSerializer
from database.serializers import ToolSerializer
from django_json_ld.views import JsonLdContextMixin
from django_json_ld.views import JsonLdDetailView


class ToolDetailView(JsonLdDetailView):
    model=Tool

class DatabaseDetailView(JsonLdDetailView):
    model=Database


def name_service(request, id):

    a_list = Service.objects.filter(id=id)
    context = {'id': id, 'service_list': a_list}
    return render(request, 'database/name_service.html', context)

def name_tool(request, id):

    a_list = Tool.objects.filter(id=id)
    context = {'id': id, 'tool_list': a_list}
    return render(request, 'database/name_tool.html', context)

def name_database(request, id):

    a_list = Database.objects.filter(id=id)
    context = {'id': id, 'database_list': a_list}
    return render(request, 'database/name_database.html', context)

def name_event(request, id):

    a_list = Event.objects.filter(id=id)
    context = {'id': id, 'event_list': a_list}
    return render(request, 'database/name_events.html', context)

def name_platform(request, id):

    a_list = Platform.objects.filter(id=id)
    context = {'id': id, 'platform_list': a_list}
    return render(request, 'database/name_platforms.html', context)

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

def tools_search(request):
    tools_list = Tool.objects.all()
    tools_filter = ToolFilter(request.GET, queryset=tools_list)
    return render(request, 'database/tools_list.html', {'filter': tools_filter})

def databases_search(request):
    databases_list = Database.objects.all()
    databases_filter = DatabaseFilter(request.GET, queryset=databases_list)
    return render(request, 'database/databases_list.html', {'filter': databases_filter})

def events_search(request):
    events_list = Event.objects.all()
    events_filter = DatabaseFilter(request.GET, queryset=events_list)
    return render(request, 'database/events_list.html', {'filter': events_filter})

def platforms_search(request):
    platforms_list = Platform.objects.all()
    platforms_filter = DatabaseFilter(request.GET, queryset=platforms_list)
    return render(request, 'database/platforms_list.html', {'filter': platforms_filter})

def index(request):
    return render(request, 'database/template.html')


    return HttpResponse("Welcome to the Catalogue of French resources in bioinformatics")



class ServiceViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allows users to be viewed or edited.
     """
     queryset = Service.objects.all().order_by('-name')
     serializer_class = serializers.ServiceSerializer
     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
     filterset_fields = ['name','year_created']



class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tool.objects.all().order_by('-name')
    serializer_class = serializers.ToolSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]


    def get_queryset(self):
        name = self.request.GET.get("name", None)
        if name:
            querysetfilter = Tool.objects.filter(name=name)
        else:
            querysetfilter = Tool.objects.all().order_by('-name')
        return querysetfilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        dict_new_data = []
        for elem in queryset:
            dict_new_data.append(elem.sd())


        return Response(dict_new_data)



class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all().order_by('-name')
    serializer_class = serializers.DatabaseSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]

    @api_view(['GET'])
    def database_list(request):
        response_data = {"data": []}
        if request.database:
            response_data["data"] = serializers.DatabaseSerializer(
                context={'@context': 'https://schema.org',},
                many=True
            ).data
            return Response(response_data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-name')
    serializer_class = serializers.EventSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]

class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all().order_by('-name')
    serializer_class = serializers.FormationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]

class Training_materialViewSet(viewsets.ModelViewSet):
    queryset = Training_material.objects.all().order_by('-name')
    serializer_class = serializers.Training_materialSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all().order_by('-name')
    serializer_class = serializers.PlatformSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all().order_by('-name')
    serializer_class = serializers.ResourceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]

