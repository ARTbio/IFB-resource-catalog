from django.db import models

from database.model.resource import *
from database.model.keyword import *

from database.model.tool_model.toolType import *
from database.model.tool_model.language import *
from database.model.tool_model.topic import *
# from database.model.tool_model.publication import *
from database.model.tool_model.elixirPlatform import *
from database.model.tool_model.elixirNode import *
from database.model.tool_model.operatingSystem import *
from database.model.tool_model.toolCredit import *
# from database.model.tool_model.function import *

from database.model.platform_model.platform import *

class Tool(Resource):
    OPERATING_SYSTEM_CHOICES = (
        ('LINUX', 'Linux'),
        ('WINDOWS', 'Windows'),
        ('MAC', 'Mac')
    )

    # tool_type = models.ForeignKey(ToolType, null=True, blank=True, related_name='toolType', on_delete=models.CASCADE)

    biotoolsID = models.CharField(blank=False, null=False, max_length=100)
    biotoolsCURIE = models.CharField(blank=False, null=False, max_length=109) #because of biotools: prefix

    # software_version = models.CharField(max_length=200, blank=True, null=True)

    citations = models.CharField(max_length=1000, blank=True, null=True)
    logo = models.URLField(max_length=200, blank=True, null=True)
    access_condition = models.TextField( blank=True, null=True)
    contact_support = models.CharField(max_length=1000, blank=True, null=True)

    tool_license = models.CharField(max_length=1000, blank=True, null=True)
    # link = models.CharField(max_length=1000, blank=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    prerequisites = models.TextField( blank=True, null=True)
    # operating_system = models.CharField(max_length=50, blank=True, null=True, choices=OPERATING_SYSTEM_CHOICES)
    # topic = models.CharField(max_length=1000, blank=True, null=True)
    # downloads = models.CharField(max_length=1000, blank=True, null=True)

    annual_visits = models.IntegerField(blank=True, null=True)
    unique_visits = models.IntegerField(blank=True, null=True)

    # many_to_many
    platform = models.ManyToManyField(Platform, blank=True)
    tool_type = models.ManyToManyField(ToolType, blank=True)
    language = models.ManyToManyField(Language, blank=True)
    topic = models.ManyToManyField(Topic, blank=True)
    # publication = models.ManyToManyField(Publication, blank=True)
    collection = models.ManyToManyField(Collection, blank=True)
    elixir_platform = models.ManyToManyField(ElixirPlatform, blank=True)
    elixir_node = models.ManyToManyField(ElixirNode, blank=True)
    accessibility = models.ManyToManyField(Accessibility, blank=True)
    operatingSystem = models.ManyToManyField(OperatingSystem, blank=True)
    toolCredit = models.ManyToManyField(ToolCredit, blank=True)

    # link = models.ManyToManyField(Link, blank=True)

    # added fields
    # language = models.CharField(max_length=1000, null=True, blank=True)
    # otherID = models.CharField(max_length=1000, null=True, blank=True)
    maturity = models.CharField(max_length=1000, null=True, blank=True)
    homepage = models.CharField(max_length=1000, null=True, blank=True)
    # collectionID = models.CharField(max_length=1000, null=True, blank=True)
    # credit = models.TextField(null=True, blank=True)
    # elixirNode = models.CharField(max_length=1000, null=True, blank=True)
    # elixirPlatform = models.CharField(max_length=1000, null=True, blank=True)
    cost = models.CharField(max_length=1000, null=True, blank=True)
    # accessibility = models.CharField(max_length=1000, null=True, blank=True)
    # function = models.TextField(null=True, blank=True)
    # relation = models.CharField(max_length=1000, null=True, blank=True)

    # to remove ?
    input_data = models.CharField(max_length=1000, blank=True, null=True)
    output_data = models.CharField(max_length=1000, blank=True, null=True)
    primary = models.CharField(max_length=1000, blank=True, null=True)

    # metadata
    additionDate = models.DateTimeField(blank=True, null=True)
    lastUpdate = models.DateTimeField(auto_now=True)

    def sd(self):
        list_pf = []
        qs = Tool.objects.all().filter(name=self.name)
        for tool in qs:
            for pf in tool.platform.all():
                list_pf.append(str(pf))
        test_json = json.dumps({'test': 'test2'})
        ctx = {
                    "@context":
                        {
                        "edam": "http://edamontology.org/",
                        "schema": "http://schema.org/",
                        "dc": "http://purl.org/dc/terms/",
                        }}

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
                                "schema:name": test_json,
                            }
                        }]
                 }
