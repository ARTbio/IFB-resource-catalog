from django.urls import path

from . import views
from .views import ServiceListView

urlpatterns = [
    path('', views.index, name='index'),
    path('services', ServiceListView.as_view(), name='service-list'),
    path('services/<int:id>/', views.name_service, name='service-detail'),
    path('list', views.service_list),
    path('search', views.search, name='search'),
]