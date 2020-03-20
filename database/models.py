import datetime
from django.conf import settings
import requests

from django.db import models
from django.urls import reverse


from database.model.tool_model.accessibility import *
from database.model.tool_model.collection import *

from database.model.tool_model.language import *
from database.model.tool_model.link import *
from database.model.tool_model.function import *
from database.model.tool_model.operatingSystem import *
from database.model.tool_model.publication import *
from database.model.tool_model.tool import *
from database.model.tool_model.topic import *
from database.model.tool_model.download import *
from database.model.tool_model.documentation import *

from database.model.resource import *
from database.model.keyword import *

from database.model.service_model.service import *
# from database.model.service_model.credit import *
# from database.model.service_model.elixirCommunities import *

# from database.model.operatingSystem import OperatingSystem

import json

"""
class Dataset(models.Model):
    identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    alternateName = models.CharField(max_length=100)
    datePublished = models.DateTimeField(default=datetime.now, blank=True)
    description = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    licence = models.CharField(max_length=100)
    citation = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    distribution = models.CharField(max_length=100)
    includeInDataCatalogue = models.CharField(max_length=100)
    measurementTechnique = models.CharField(max_length=100)
    variableMeasured = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Function(models.Model):
    operation = models.CharField(max_length=100)
    input = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    cmd = models.CharField(max_length=100)
    term = models.CharField(max_length=100)

class Labels(models.Model):
    toolType = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    operatingSystem = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    license = models.CharField(max_length=100)
    collectionID = models.CharField(max_length=100)
    maturity = models.CharField(max_length=100)
    cost = models.IntegerField()
    accessibility = models.CharField(max_length=100)

class Link(models.Model):
    url = models.URLField(max_length=200)
    type = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)

class Download(models.Model):
    link = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    type = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)

class Documentation(models.Model):
    url = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    cmd = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

class Publication(models.Model):
    doi = models.CharField(max_length=100)
    pmid = models.CharField(max_length=100)
    pmcid = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

class Credit(models.Model):
    name = models.CharField(max_length=100)
    orcidid = models.CharField(max_length=100)
    gridid = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    tel = models.CharField(max_length=100)
    typeEntity = models.CharField(max_length=100)
    typeRole = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    homepage = models.URLField()
    biotoolsID = models.CharField(max_length=100)
    biotoolsCURIE = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    otherID = models.CharField(max_length=100)
    featureList = models.CharField(max_length=100)
    rdf:type= models.CharField(max_length=100)
    softwareVersion = models.CharField(max_length=100)
    url = models.URLField()
    citation = models.CharField(max_length=100)
    license = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    applicationCategory = models.CharField(max_length=100)
    date_created = models.DateTimeField(blank=True)
    date_modified = models.DateTimeField(blank=True)
    has_part = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    offers = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    potentialAction = models.CharField(max_length=100)
    softwareHelp = models.CharField(max_length=100)
    software_requirements = models.CharField(max_length=100)
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    labels = models.ForeignKey(Labels, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    download = models.ForeignKey(Download, on_delete=models.CASCADE)
    documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


"""


TITLE_MATURITY = (
    ('EMERGING', 'Emerging'),
    ('MATURE', 'Mature'),
    ('LEGACY', 'Legacy'),
)























class Database(Resource):
    logo = models.URLField(max_length=200, blank=True, null=True)
    access_conditions = models.TextField()
    citations = models.CharField(max_length=1000, blank=True, null=True)
    link_data = models.CharField(max_length=1000, blank=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    annual_visits = models.IntegerField( blank=True, null=True)
    unique_visits = models.IntegerField( blank=True, null=True)
    last_update = models.DateTimeField( blank=True, null=True)
    increase_last_update = models.CharField(max_length=1000, blank=True, null=True)
    platform = models.ManyToManyField(Platform)

    def sd(self):
        return {
            "@context":
                {
                "edam": "http://edamontology.org/",
                "schema": "http://schema.org/",
                "dc": "http://purl.org/dc/terms/",
                },
            "@id": settings.VAR_URL+"api/?name="+self.name,
            "@language": "fr",
            "@type": "schema:WebAPI",
            "name": "CatalogRestToolAPI",
            "@graph":
                [{
                "@id": "https://www.france-bioinformatique.fr/en/services/outils/"+self.name,
                "@type": "schema:SoftwareApplication",
                "schema:name": self.name,
                "schema:description": self.description,
                "schema:laboratoryScience":
                    {
                        "@type": "schema:LaboratoryScience",
                        "schema:name": self.platform.name,
                    }
                }]
                }


class Event(Resource):
    logo = models.URLField(max_length=200, blank=True, null=True)
    event_type = models.CharField(max_length=1000, blank=True, null=True)
    start_date = models.DateTimeField( blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)
    organizer = models.CharField(max_length=1000, blank=True, null=True)
    sponsors = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

class Formation(Resource):
    logo = models.URLField(max_length=200, blank=True, null=True)
    formation_type = models.CharField(max_length=1000, blank=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    start_date = models.DateTimeField( blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    access_conditions = models.TextField()
    link = models.CharField(max_length=1000, blank=True, null=True)
    organizer = models.CharField(max_length=1000, blank=True, null=True)
    sponsors = models.CharField(max_length=1000, blank=True, null=True)
    number_people_trained = models.IntegerField( blank=True, null=True)
    number_of_academic_participants = models.IntegerField( blank=True, null=True)
    number_of_non_academic_participants = models.IntegerField( blank=True, null=True)
    training_time = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    participation = models.CharField(max_length=1000, blank=True, null=True)
    training_level = models.CharField(max_length=1000, blank=True, null=True)
    training_operator = models.CharField(max_length=1000, blank=True, null=True)
    number_of_sessions = models.IntegerField( blank=True, null=True)
    recurrence = models.CharField(max_length=1000, blank=True, null=True)
    satisfaction_rate = models.CharField(max_length=1000, blank=True, null=True)
    platform = models.ManyToManyField(Platform)

    def __str__(self):
        return self.name

class Training_material(Resource):
    file_name = models.CharField(max_length=1000, blank=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    licence = models.CharField(max_length=1000, blank=True, null=True)
    event_link = models.CharField(max_length=1000, blank=True, null=True)
    publication_date = models.DateTimeField(blank=True)
    target_audience = models.CharField(max_length=1000, blank=True, null=True)
    url_file = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name



# class Link(models.Model):
# 	# name = models.CharField(max_length=100, blank=True, null=True)
#     url = models.CharField(max_length=200, blank=True, null=True)
#     type = models.CharField(max_length=100, blank=True, null=True)
#     note = models.CharField(max_length=1000, blank=True, null=True)
#     tool = models.ForeignKey(Tool, null=True, blank=True, related_name='link', on_delete=models.CASCADE)
#
#     # metadata
#     additionDate = models.DateTimeField(auto_now_add=True)
#
#     def __unicode__(self):
#         return unicode(self.name) or u''



class Relation(models.Model):
    biotoolsID = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=100, blank=False, null=False)
    tool = models.ForeignKey(Tool, null=True, blank=True, related_name='relation', on_delete=models.CASCADE)

     # metadata
    additionDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name) or u''

class OtherID(models.Model):
    value = models.CharField(blank=False, null=False, max_length=1000, unique=False)
    type = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    tool = models.ForeignKey(Tool, null=True, blank=True, related_name='otherID', on_delete=models.CASCADE)

    # metadata
    additionDate = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return unicode(self.value) or u''

class Version(models.Model):
    version = models.CharField(max_length=100, blank=True, null=True)
    tool = models.ForeignKey(Tool, null=True, blank=True, related_name='version', on_delete=models.CASCADE)

     # metadata
    additionDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name) or u''
