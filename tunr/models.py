from django.db import models

# Create your models here.

# tunr/models.py
class Decade(models.Model):
    name = models.CharField(max_length=20)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name

class Fad(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name

