from django.db import models

class Resource(models.Model):
    # name = models.CharField(max_length=1000, blank=True, null=True, unique=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
