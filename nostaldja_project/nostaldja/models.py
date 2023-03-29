from django.db import models

# Create your models here.

class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fad(models.Model):
    decades = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fad')
    name = models.CharField(max_length=100, default='no title')
    image_url = models.TextField(null=True)
    decade = models.CharField(max_length=100)

    def __str__(self):
        return self.name