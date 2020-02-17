from django.db import models

class TypeRole(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    # metadata
    additionDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name) or u''

class ToolCredit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    orcidid = models.CharField(max_length=100, blank=True, null=True)
    gridid = models.CharField(max_length=100, blank=True, null=True)
    typeEntity = models.CharField(max_length=100, blank=True, null=True)
    # typeRole = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=2000, blank=True, null=True)

    # many to many
    typeRole = models.ManyToManyField(TypeRole, blank=True)

    def __unicode__(self):
        return unicode(self.name) or u''
