from django.db import models
from database.models import *

# TODO
class Topic(models.Model):
	# topic should not be mandatory

	uri = models.CharField(max_length=100, blank=True, null=True)
	term = models.CharField(max_length=100, blank=True, null=True)

    # tool = models.ForeignKey(Tool, null=True, blank=True, related_name='topic', on_delete=models.CASCADE)


	# metadata
	additionDate = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.term) or u''
