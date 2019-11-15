from .models import Service
from .models import Tool
from .models import Database
import django_filters
from django import forms

class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['maturity', 'year_created', 'is_tool', 'is_data', 'is_training', 'is_compute', 'is_interoperability']


class ToolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tool
        fields = ['name']


class DatabaseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Database
        fields = ['name']
