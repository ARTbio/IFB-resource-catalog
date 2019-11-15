import datetime
from django.conf import settings
import requests
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

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


TITLE_INFRA = (
    ('PROPRIETAIRE', 'Propriétaire'),
    ('HEBERGEE', 'Hébergée'),
)


class Credit(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    laboratory = models.CharField(max_length=1000)
    institute = models.CharField(max_length=1000)
    adress = models.CharField(max_length=1000, null=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ElixirCommunities(models.Model):
    name = models.CharField(max_length=10000)
    class Meta:
        verbose_name_plural = "Elixir Communities"

    def __str__(self):
        return self.name

class Publication(models.Model):
    doi = models.CharField(max_length=100)

    def __str__(self):
        return self.doi

class ToolType(models.Model):
    name = models.CharField(max_length=10000)

    def __str__(self):
        return self.name

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Resource(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Service(Resource):
    credit = models.ManyToManyField(Credit)
    scope = models.TextField()
    is_tool = models.BooleanField(default=False)
    is_data = models.BooleanField(default=False)
    is_training = models.BooleanField(default=False)
    is_compute = models.BooleanField(default=False)
    is_interoperability = models.BooleanField(default=False)
    communities = models.TextField()
    elixir_communities = models.ManyToManyField(ElixirCommunities, blank=True)
    year_created = models.IntegerField(('year'), validators=[MinValueValidator(1984), max_value_current_year],null=True)
    maturity = models.TextField(max_length=8, choices=TITLE_MATURITY)
    access = models.TextField()
    quality = models.TextField()
    usage = models.TextField()
    publication_citations_nb = models.IntegerField()
    publication_coauthor_nb = models.IntegerField()
    key_pub = models.ManyToManyField(Publication, blank=True)
    sab_user_comittee = models.TextField()
    term_of_use = models.TextField()
    ethics_policy = models.TextField()
    funding = models.TextField()
    motivation_catalog = models.BooleanField(default=False)
    motivation_sdp = models.BooleanField(default=False)
    motivation_support_ifb_it = models.BooleanField(default=False)
    motivation_support_ifb_curation = models.BooleanField(default=False)
    motivation_support_ifb_core_resource = models.BooleanField(default=False)
    biotoolsID = models.CharField(max_length=1000, null=True, blank=True)
    toolType = models.ManyToManyField(ToolType)

    def topics(self):
        topics=[]
        i=0
        if self.biotoolsID:
            get_data = requests.get("https://bio.tools/api/"+self.biotoolsID+"?format=json")
            response_data = get_data.json()
            while i < len(response_data["topic"]):
                topics.append(response_data["topic"][i]["term"])
                i=i+1
                continue
            return topics


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('database:service-detail' ,args=[self.pk])

class Keyword(models.Model):
    name = models.CharField(max_length=10000)
    def __str__(self):
        return self.name

class Activityarea(models.Model):
    name = models.CharField(max_length=10000)
    def __str__(self):
        return self.name

class Certificat(models.Model):
    name = models.CharField(max_length=10000)
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Platform(Resource):
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
    infrastructure_type = models.TextField(max_length=13, choices=TITLE_INFRA, blank=True, null=True)
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

class Tool(Resource):
    citations = models.CharField(max_length=1000, blank=True, null=True)
    logo = models.URLField(max_length=200, blank=True, null=True)
    access_condition = models.TextField( blank=True, null=True)
    contact_support = models.CharField(max_length=1000, blank=True, null=True)
    input_outils = models.CharField(max_length=1000, blank=True, null=True)
    tool_license = models.CharField(max_length=1000, blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    prerequisites = models.TextField( blank=True, null=True)
    operating_system = models.CharField(max_length=1000, blank=True, null=True)
    tool_type = models.ManyToManyField(ToolType, blank=True)
    downloads = models.IntegerField(blank=True, null=True)
    software_version = models.IntegerField(blank=True, null=True)
    annual_visits = models.IntegerField(blank=True, null=True)
    unique_visits = models.IntegerField(blank=True, null=True)
    platform = models.ManyToManyField(Platform, blank=True)

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




