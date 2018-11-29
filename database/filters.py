from .models import Service
import django_filters
from django import forms

class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['maturity', 'year_created', 'is_tool', 'is_data', 'is_training', 'is_compute', 'is_interoperability']
