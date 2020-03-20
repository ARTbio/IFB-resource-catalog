from django.db import models

from database.model.resource import *

from database.model.tool_model.publication import *

from database.model.service_model.credit import *
from database.model.service_model.elixirCommunities import *

from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)




class Service(Resource):
    MATURITY_CHOICES = (
        ('EMERGING', 'Emerging'),
        ('MATURE', 'Mature'),
        ('LEGACY', 'Legacy'),
    )

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
    maturity = models.TextField(max_length=8, choices=MATURITY_CHOICES)
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
