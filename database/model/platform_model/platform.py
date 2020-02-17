from django.db import models

from database.model.resource import *
from database.model.keyword import *

from database.model.platform_model.people import *
from database.model.platform_model.certificat import *
from database.model.platform_model.activityArea import *

class Platform(Resource):
    INFRA_CHOICES = (
        ('PROPRIETAIRE', 'Propriétaire'),
        ('HEBERGEE', 'Hébergée'),
    )

    logo = models.URLField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    affiliation = models.CharField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)
    scientific_leader = models.ManyToManyField(People, blank=True, related_name="scientific_leader_of")
    technical_leader = models.ManyToManyField(People, blank=True, related_name="technical_leader_of")
    certificate = models.ManyToManyField(Certificat, blank=True)
    structure = models.CharField(max_length=1000, blank=True, null=True)
    activity_area = models.ManyToManyField(Activityarea, blank=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    infrastructure_type = models.TextField(max_length=13, choices=INFRA_CHOICES, blank=True, null=True)
    useful_storage_capacity = models.CharField(max_length=1000, blank=True, null=True)
    cpu_number = models.IntegerField( blank=True, null=True)
    data_collection = models.CharField(max_length=1000, blank=True, null=True)
    cpu_hour_per_year = models.CharField(max_length=1000, blank=True, null=True)
    informatics_tools = models.CharField(max_length=1000, blank=True, null=True)
    users_number = models.IntegerField( blank=True, null=True)
    support_condition = models.TextField( blank=True, null=True)
    server_description = models.TextField( blank=True, null=True)
    title_project_support = models.CharField(max_length=1000, blank=True, null=True)
    description_projects_help = models.TextField( blank=True, null=True)
    accompanied_project = models.TextField( blank=True, null=True)
    hosted_projects = models.TextField( blank=True, null=True)
    publications = models.CharField(max_length=1000, blank=True, null=True)
    team = models.ManyToManyField(People, blank=True, related_name="member_of")
    def __str__(self):
        return self.name
