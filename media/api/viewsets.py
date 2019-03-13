from media.models import Media
from rest_framework.viewsets import ModelViewSet
from media.api.serializers import MediaSerializer

class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer