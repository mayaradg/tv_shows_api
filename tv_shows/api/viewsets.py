from rest_framework.viewsets import ModelViewSet
from tv_shows.models import TvShow
from .serializers import TvShowSerializer

class TvShowViewSet(ModelViewSet):
    queryset = TvShow.objects.all()
    serializer_class = TvShowSerializer