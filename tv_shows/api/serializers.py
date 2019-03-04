from rest_framework.serializers import ModelSerializer
from tv_shows.models import TvShow

class TvShowSerializer(ModelSerializer):
    class Meta:
        model = TvShow
        fields = ('id', 'name', 'genre', 'storyline')