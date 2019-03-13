from rest_framework.serializers import ModelSerializer
from rates.models import Rate

class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'rate','commentary', 'tv_show', 'user')