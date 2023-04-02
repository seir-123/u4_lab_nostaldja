from django.db import models

# Create your models here.
class Decade(models.Model):
  name = models.CharField(max_length=100)
  start_year = models.CharField(max_length=5)
  end_year = models.CharField(max_length=5)

  def __str__(self):
      return self.name

class Fad(models.Model): 
  name = models.CharField(max_length=100)
  image_url = models.CharField(max_length=200, null=True)
  description = models.CharField(max_length=100, default='no album title')
  decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

  def __str__(self):
      return self.name
  