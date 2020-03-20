from django.db import models
from database.model.tool_model.tool import *

class Documentation(models.Model):
	url = models.TextField()
	type = models.TextField()
	note = models.TextField(blank=True, null=True)
	tool = models.ForeignKey(Tool, null=True, blank=True, related_name='documentation', on_delete=models.CASCADE)

	# metadata
	additionDate = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.url) or u''
