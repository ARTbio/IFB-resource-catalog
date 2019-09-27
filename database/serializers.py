from rest_framework import serializers

from database import models



class CreditSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Credit
        fields = ('name', 'laboratory', 'institute', 'adress', 'email')

class ElixirCommunitiesSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ElixirCommunities
        fields = ('name',)

class PublicationSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Publication
        fields = ('doi',)

class ToolTypeSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ToolType
        fields = ('name',)


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    credit = CreditSerialize(read_only=True, many=True)
    elixir_communities = ElixirCommunitiesSerialize(read_only=True, many=True)
    key_pub = PublicationSerialize(read_only=True, many=True)
    toolType = ToolTypeSerialize(read_only=True, many=True)


    class Meta:
        model = models.Service
        fields = ('name', 'credit' , 'scope', 'is_tool', 'is_data', 'is_training', 'is_compute', 'is_interoperability', 'description', 'communities', 'elixir_communities', 'year_created', 'maturity', 'access', 'quality', 'usage', 'publication_citations_nb', 'publication_coauthor_nb', 'key_pub', 'sab_user_comittee', 'term_of_use', 'ethics_policy', 'biotoolsID' ,'toolType')
        depth = 2