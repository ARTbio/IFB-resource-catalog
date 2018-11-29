from django.contrib import admin
from .models import Credit
from .models import ElixirCommunities
from .models import Publication
from .models import Service



class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'credit',
        'elixir_communities',
        'key_pub',
    )

admin.site.register(Service, ServiceAdmin)
admin.site.register(Credit)
admin.site.register(ElixirCommunities)
admin.site.register(Publication)
