from django.contrib import admin
from django.contrib.admin.options import get_content_type_for_model
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext

from .models import Activityarea
from .models import Credit
from .models import Database
from .models import ElixirCommunities
from .models import Event
from .models import Formation
from .models import Keyword
from .models import People
from .models import Platform
from .models import Publication
from .models import Service
from .models import Tool
from .models import ToolType
from .models import Training_material


# Admin interface configuration
class ViewOnSiteModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',)
        }

    def __init__(self, model, admin_site):
        if callable(getattr(model, "get_absolute_url", None)) and callable(self.view_on_site_in_list):
            self.list_display += ('view_on_site_in_list',)
        super().__init__(model, admin_site)

    def view_on_site_in_list(self, obj):
        return format_html(
            '<center><a href="' + reverse('admin:view_on_site', kwargs={
                'content_type_id': get_content_type_for_model(obj).pk,
                'object_id': obj.pk
            }) + '"><i class="fa fa-external-link"></i></a><center>')

    view_on_site_in_list.short_description = format_html('<center>' + ugettext('View on site') + '<center>')



#choose the fields to be displayed in the admin interface
class ServiceAdmin(ViewOnSiteModelAdmin):
    filter_horizontal = (
        'credit',
        'elixir_communities',
        'key_pub',
    )
    list_display = ('name','biotoolsID','year_created')
    search_fields = (
        'name',
        'biotoolsID',
        'year_created',
        'credit__name',
        'credit__laboratory',
        'credit__institute',
        'elixir_communities__name',
        'key_pub__doi',
    )

class ToolAdmin(ViewOnSiteModelAdmin):
    list_display = ('name','description')

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PlatformAdmin(ViewOnSiteModelAdmin):
    list_display = ('name',)

class DatabaseAdmin(ViewOnSiteModelAdmin):
    list_display = ('name',)
    date_hierarchy = 'last_update'

#Declare the models to be displayed in admin interface
admin.site.register(Service, ServiceAdmin)
admin.site.register(Credit)
admin.site.register(ElixirCommunities)
admin.site.register(Publication)
admin.site.register(ToolType)
admin.site.register(Training_material)
admin.site.register(People)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Event)
admin.site.register(Formation)
admin.site.register(Database, DatabaseAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Activityarea)
admin.site.register(Keyword, KeywordAdmin)