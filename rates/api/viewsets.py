from rest_framework.viewsets import ModelViewSet
from rates.models import Rate
from rates.api.serializers import RateSerializer

class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
