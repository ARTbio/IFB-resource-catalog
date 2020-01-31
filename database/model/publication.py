from django.db import models
from database.models import *

class Publication(models.Model):
    doi = models.CharField(max_length=100, blank=True, null=True)
    pmid = models.CharField(max_length=50, blank=True, null=True)
    pmcid = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.doi
