from django.db import models
from database.models import *

class OperatingSystem(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	tool_id = models.ForeignKey(Tool, null=True, blank=True, related_name='operatingSystem', on_delete=models.CASCADE)

	# metadata
	additionDate = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.name) or u''
