from django.db import models

# Create your models here.
class Yarn(models.Model):
  name = models.CharField(max_length=100)
  weight = models.CharField(max_length=50)
  fiber = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name