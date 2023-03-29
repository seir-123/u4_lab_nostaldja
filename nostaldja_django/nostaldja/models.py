from django.db import models


class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

def __str__(self):
    return self.name

class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100, default='no decade name')
    description = models.CharField(max_length=100, default='no descritption name')
    image_url = models.TextField(null=True)

def __str__(self):
    return self.name