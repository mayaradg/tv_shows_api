from django.db import models
from genres.models import Genre

# Create your models here.
class TvShow(models.Model):
    name = models.CharField(max_length=30)
    storyline = models.TextField()
    average = models.DecimalField(decimal_places=1, max_digits=3)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)