from django.db import models
from genres.models import Genre

# Create your models here.
class TvShow(models.Model):
    name = models.CharField(max_length=30)
    storyline = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
