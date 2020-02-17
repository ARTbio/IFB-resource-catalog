from django.db import models
from database.model.tool_model.tool import *

class Publication(models.Model):
    doi = models.CharField(max_length=100, blank=True, null=True)
    pmid = models.CharField(max_length=50, blank=True, null=True)
    pmcid = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    tool = models.ForeignKey(Tool, null=True, blank=True, related_name='publication', on_delete=models.CASCADE)

    # metadata
    additionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doi
