from django.db import models
from django.contrib.auth.models import User
from tv_shows.models import TvShow

class Rate(models.Model):
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    commentary = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv_show = models.ForeignKey(TvShow, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rate)
