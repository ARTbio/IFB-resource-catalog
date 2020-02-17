from django.db import models
from database.model.tool_model.tool import *

class Download(models.Model):
	# name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    tool = models.ForeignKey(Tool, null=True, blank=True, related_name='download', on_delete=models.CASCADE)

    # metadata
    additionDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name) or u''
