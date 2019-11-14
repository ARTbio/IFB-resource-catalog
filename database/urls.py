from django.urls import path

from database import views

app_name = 'database'
urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.ServiceListView.as_view(), name='service-list'),
    path('services/<int:id>/', views.name_service, name='service-detail'),
    path('tools/<int:id>/', views.name_tool, name='tool-detail'),
    path('list', views.service_list),
    path('search', views.search, name='search'),
]