from django.db import models
from database.models import *

class Collection(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	# metadata
	additionDate = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.name) or u''
