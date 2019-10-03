from rest_framework import serializers

from database import models



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

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    team = PeopleSerializer(read_only=True, many=True)

    class Meta:
        model = models.Platform
        fields = ('name', 'logo', 'address', 'website', 'team')

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
    keyword = KeywordSerializer(read_only=True, many=True)
    tool_type = ToolTypeSerializer(read_only=True, many=True)
    platform = PlatformSerializer(read_only=True, many=True)

    class Meta:
        model = models.Tool
        fields = ('name', 'description', 'tool_type', 'keyword', 'platform')
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

class FormationSerializer(serializers.HyperlinkedModelSerializer):
    people = PeopleSerializer(read_only=True, many=True)
    certificate = CertificatSerializer(read_only=True, many=True)
    keyword = KeywordSerializer(read_only=True, many=True)
    platform = PlatformSerializer(read_only=True, many=True)

    class Meta:
        model = models.Formation
        fields = ('name', 'formation_type', 'description', 'link')

class Training_materialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Training_material
        fields = ('name', 'description', 'file_name')