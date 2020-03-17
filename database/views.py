from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.views import APIView
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

from .model.tool_model.operatingSystem import *
from .model.tool_model.topic import *
from .model.tool_model.publication import *
from .model.tool_model.function import *
from .model.tool_model.documentation import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from database.serializers import DatabaseSerializer
from database.serializers import ToolSerializer
from django_json_ld.views import JsonLdContextMixin
from django_json_ld.views import JsonLdDetailView

import json
from rdflib import ConjunctiveGraph
import logging



class ToolDetailView(JsonLdDetailView):
    model=Tool

class DatabaseDetailView(JsonLdDetailView):
    model=Database


def name_service(request, id):

    a_list = Service.objects.filter(id=id)
    context = {'id': id, 'service_list': a_list}
    return render(request, 'database/name_service.html', context)

def name_tool(request, id):
    logger = logging.getLogger(__name__)
    a_list = Tool.objects.filter(id=id)



    logger.info('something here')
    ctx = {
        "@context": {
            "@base": "https://bio.tools/",
            "biotools": "https://bio.tools/ontology/",
            "edam": "http://edamontology.org/",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "sc": "http://schema.org/",
            "bsc": "http://bioschemas.org/",

            "description": 'sc:description',
            "name": "sc:name",
            "homepage": "sc:url",
            "toolType": 'sc:additionalType',


            "primaryContact": 'biotools:primaryContact',
            "author": 'sc:author',
            "provider": 'sc:provider',
            "contributor": 'sc:contributor',
            "funder": 'sc:funder',
            "hasPublication": "sc:citation",

            "hasTopic": 'sc:applicationSubCategory',
            "hasOperation": "sc:featureList",
            "hasInputData": "edam:has_input",
            "hasOutputData": "edam:has_output",

            "license": "sc:license",
            "version": "sc:version",
            "isAccessibleForFree" : "sc:isAccessibleForFree",
            "operatingSystem": "sc:operatingSystem",
            "hasDoc": "sc:softwareHelp",
            "hasTermsOfUse": "sc:termsOfService",
        }
    }

    entry = a_list
    print(a_list.values())
    jld = json.loads("{}")
    jld.update(ctx)

    jld['@id'] = entry.values_list('biotoolsID', flat=True).get()
    #entry['@type'] = ['bsc:Tool','sc:SoftwareApplication']
    jld['@type'] = ['sc:SoftwareApplication']
    jld['applicationCategory'] = 'Computational science tool'
    jld['name'] = entry.values_list('name', flat=True).get()
    jld['description'] = entry.values_list('description', flat=True).get()
    jld['homepage'] = entry.values_list('homepage', flat=True).get()
    jld['isAccessibleForFree'] = entry.values_list('cost', flat=True).get()
    jld['license'] = entry.values_list('tool_license', flat=True).get()

    # Getting OS
    operatingSystem = OperatingSystem.objects.filter(tool__id=id)
    if operatingSystem.values_list('name', flat=True):
        jld['operatingSystem'] = []
        for os in operatingSystem.values_list('name', flat=True):
            jld['operatingSystem'].append(os)

    # Getting toolType
    toolTypes = ToolType.objects.filter(tool__id=id)
    if toolTypes.values_list('name', flat=True):
        jld['toolType'] = []
        for toolType in toolTypes.values_list('name', flat=True):
            jld['toolType'].append(toolType)

    # Getting topic
    topics = Topic.objects.filter(tool__id=id)
    if topics.values_list('term', flat=True):
        jld['hasTopic'] = []
        for topic in topics.values_list('term', flat=True):
            jld['hasTopic'].append(topic)

    # Getting publication
    publications = Publication.objects.filter(tool__id=id)
    if publications.values_list('doi', flat=True):
        jld['hasPublication'] = []
        for publication in publications.values_list('doi', flat=True):
            jld['hasPublication'].append(publication)

    # Getting documentation
    documentations = Documentation.objects.filter(tool__id=id)
    if documentations.values_list('url', flat=True):
        jld['hasDoc'] = []
        for documentation in documentations.values_list('url', flat=True):
            jld['hasDoc'].append(documentation)

    # Getting operation
    functions = Function.objects.filter(tool__id=id)
    function_id = list(functions.values_list('id', flat=True))
    for id in function_id:
        operations = Operation.objects.filter(function__id=id)
        if operations.values_list('term', flat=True):
            jld['hasOperation'] = []
            for operation in operations.values_list('term', flat=True):
                jld['hasOperation'].append(operation)

    # Getting input
    for id in function_id:
        inputs = Input.objects.filter(function__id=id)
        inputs_id = inputs.values_list('data_id', flat=True)
        if inputs_id:
            for id in inputs_id:
                data = Data.objects.filter(input__id=id)
                jld['hasInputData'] = []
                for input_data in data.values_list('term', flat=True):
                    jld['hasInputData'].append(input_data)

    # Getting output
    for id in function_id:
        outputs = Output.objects.filter(function__id=id)
        outputs_id = outputs.values_list('data_id', flat=True)
        if outputs_id:
            for id in outputs_id:
                data = Data.objects.filter(output__id=id)
                jld['hasOutputData'] = []
                for output_data in data.values_list('term', flat=True):
                    jld['hasOutputData'].append(output_data)

    jld['primaryContact'] = []
    jld['author'] = []
    jld['contributor'] = []
    jld['provider'] = []
    jld['funder'] = []

    raw_jld = json.dumps(jld, indent=4, sort_keys=True)

    g = ConjunctiveGraph()
    g.parse(data=raw_jld, format='json-ld')
    print(len(g))

    context = {'id': id, 'tool_list': a_list, 'jld': raw_jld}
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

class BiotoolsViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all().order_by('-name')
    serializer_class = serializers.BioToolsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]

# class MyOwnView(APIView):
#     def get(self, request):
#         return Response({'some': 'data'})
