from django.contrib import admin
from .models import Credit
from .models import ElixirCommunities
from .models import Publication
from .models import Service

admin.site.register(Service)
admin.site.register(Credit)
admin.site.register(ElixirCommunities)
admin.site.register(Publication)
