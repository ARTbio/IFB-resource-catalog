from django.utils import timezone
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import RedirectView
from collections import OrderedDict

from django.db.models import Max, Min, Count, F
from django.db.models.functions import Cast
from django.db.models import FloatField
from django.urls import reverse
import json
import math
from collections import OrderedDict

from django.db.models import Max, Min, Count, F
from django.db.models.functions import Cast
from django.db.models import FloatField
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.shortcuts import render
from .filters import ServiceFilter

from .models import Service, Credit, ElixirCommunities, Publication

from .filters import ServiceFilter

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



