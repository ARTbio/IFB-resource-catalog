from django.urls import path

from database import views

app_name = 'database'
urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.ServiceListView.as_view(), name='service-list'),
    path('services/<int:id>/', views.name_service, name='service-detail'),
    path('tools/<int:id>/', views.name_tool, name='tool-detail'),
    path('databases/<int:id>/', views.name_database, name='database-detail'),
    path('events/<int:id>/', views.name_event, name='event-detail'),
    path('platforms/<int:id>/', views.name_platform, name='platform-detail'),
    path('list', views.service_list),
    path('search', views.search, name='search'),
    path('tools', views.tools_search, name='tools_search'),
    path('databases', views.databases_search, name='databases_search'),
    path('events', views.events_search, name='events_search'),
    path('platforms', views.platforms_search, name='platforms_search'),
]