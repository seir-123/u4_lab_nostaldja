from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length=50)
    start_year = models.IntegerField(max_length=4)
    end_year = models.IntegerField(max_length=4)
    
    def __str__(self):
        return self.name
    
class Fads(models.Model):
    name = models.CharField(max_length = 150)
    image_url = models.CharField(max_length = 255)
    description = models.TextField(max_length = 500)
    decade = models.ForeignKey(Decade,
           on_delete = models.CASCADE,
           related_name = 'fads')
    
    def __str__(self):
        return self.name