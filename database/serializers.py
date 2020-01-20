from rest_framework import serializers

from database import models
from database.models import Database
import json



class CreditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Credit
        fields = ('name', 'laboratory', 'institute', 'adress', 'email')

class ElixirCommunitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ElixirCommunities
        fields = ('name',)

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Publication
        fields = ('doi',)

class ToolTypeSerializer(serializers.HyperlinkedModelSerializer):

    # name = serializers.SerializerMethodField()
    #
    # def get_name(self, obj):
    #     return obj.name

    class Meta:
        model = models.ToolType
        fields = ('name',)

class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Keyword
        fields = ('name',)

class CertificatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Certificat
        fields = ('name',)

class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.People
        fields = ('name',)
        depth = 2

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    team = PeopleSerializer(read_only=True, many=True)

    class Meta:
        model = models.Platform
        fields = ('name', 'logo', 'address', 'website', 'team')
        depth = 1

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    credit = CreditSerializer(read_only=True, many=True)
    elixir_communities = ElixirCommunitiesSerializer(read_only=True, many=True)
    key_pub = PublicationSerializer(read_only=True, many=True)
    toolType = ToolTypeSerializer(read_only=True, many=True)


    class Meta:
        model = models.Service
        fields = ('name', 'credit' , 'scope', 'is_tool', 'is_data', 'is_training', 'is_compute', 'is_interoperability', 'description', 'communities', 'elixir_communities', 'year_created', 'maturity', 'access', 'quality', 'usage', 'publication_citations_nb', 'publication_coauthor_nb', 'key_pub', 'sab_user_comittee', 'term_of_use', 'ethics_policy', 'biotoolsID' ,'toolType')
        depth = 2


class ToolSerializer(serializers.HyperlinkedModelSerializer):
    keywords = KeywordSerializer(read_only=True, many=True)
    toolType = ToolTypeSerializer(source='tool_type', read_only=True, many=True)
    platform = PlatformSerializer(read_only=True, many=True)
    name = serializers.CharField(help_text="Help name")

    class Meta:
        model = models.Tool
        fields = ('name', 'description', 'access_condition', 'toolType', 'keywords', 'platform')
        depth = 1

class ResourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Resource
        fields = ('name', 'description')
        depth = 2


class DatabaseSerializer(serializers.HyperlinkedModelSerializer):
    keyword = KeywordSerializer(read_only=True, many=True)
    platform = PlatformSerializer(read_only=True, many=True)

    class Meta:
        model = models.Database
        fields = ('name', 'logo', 'description', 'access_conditions', 'keyword', 'platform')
        depth = 2


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Event
        fields = ('name', 'event_type', 'description', 'link')
        depth = 2

class FormationSerializer(serializers.HyperlinkedModelSerializer):
    people = PeopleSerializer(read_only=True, many=True)
    certificate = CertificatSerializer(read_only=True, many=True)
    keyword = KeywordSerializer(read_only=True, many=True)
    platform = PlatformSerializer(read_only=True, many=True)

    class Meta:
        model = models.Formation
        fields = ('name', 'formation_type', 'description', 'link', 'platform', 'people', 'certificate', 'keyword')
        depth = 2

class Training_materialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Training_material
        fields = ('name', 'description', 'file_name')
        depth = 2

class BioToolsSerializer(serializers.HyperlinkedModelSerializer):
    keywords = KeywordSerializer(read_only=True, many=True)
    toolType = ToolTypeSerializer(source='tool_type', read_only=True, many=True)
    platform = PlatformSerializer(read_only=True, many=True)
    name = serializers.CharField(help_text="Help name")



    class Meta:
        model = models.Tool
        fields = ('name', 'description', 'access_condition', 'toolType', 'keywords', 'platform')
        depth = 1

    def to_representation(self, instance):
        # print(instance.address)
        # for attribute_name in dir(instance):
        #     print(attribute_name)
        # print(instance)
        # print(self.fields["toolType"])
        # toolType = self.fields['toolType']
        # toolType_value = toolType.to_representation(
        #     toolType.get_attribute(instance)
        # )
        # print(toolType_value)

        representation = {
            "name": instance.name,
            "description": instance.description,
            "homepage": instance.link,
            "biotoolsID": instance.biotoolsID,
            "biotoolsCURIE": instance.biotoolsCURIE,
            "version": instance.software_version,
            "otherID": "TBD",
            "toolType": self.toolType(instance.tool_type),
            "topic": self.topic(instance.topic),
            "operatingSystem": instance.operating_system,
            "language": "TBD",
            "license": instance.tool_license,
            "collectionID": "TBD",
            "maturity": "not_yet_available_for_tool",
            "cost": "TBD",
            "accessibility": instance.access_condition,
            "elixirPlatform": "TBD",
            "elixirNode": "TBD",
            "function": "TBD",
            "link": "TBD",
            "download": "TBD",
            "documentation": "TBD",
            "relation": "TBD",
            "publication": "TBD",
            "credit": "TBD"
        }
        return representation

    def topic(self, topic):
        # should generate an array of terms with a loop or something
        structured_topic = [{
            "term": topic,
            "uri": "TBD",
        }]
        return structured_topic

    def toolType(self, tooltype):
        tooltype_list = []
        for elem in tooltype.values_list('name', flat=True):
            tooltype_list.append(elem)
        # qs_json = d_serializers.serialize('json', list(instance.tool_type.all()))
        # qs_json2 = json.dumps(list(instance.tool_type.all()))
        # print(qs_json)
        # structured_tooltype = str(list(tooltype))
        # # structured_tooltype = structured_tooltype.replace("<", "").
        # structured_tooltype = ''.join(c for c in structured_tooltype if c not in '<>')
        #
        return tooltype_list
