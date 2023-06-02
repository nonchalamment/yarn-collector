from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

DUSTLEVEL = (
  ('L', 'Light'),  
  ('M', 'Medium'),
  ('H', 'Heavy')
)

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('project-detail', kwargs={'pk': self.id})
  
class Yarn(models.Model):
  name = models.CharField(max_length=100)
  weight = models.CharField(max_length=50)
  fiber = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  projects = models.ManyToManyField(Project)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('yarn-detail', kwargs={'yarn_id': self.id})
  
  def dusted_for_today(self):
    return self.dusting_set.filter(date=date.today()).count() >= 1
  
class Dusting(models.Model):
  date = models.DateField('Dusting date')
  dust = models.CharField(
    max_length=1,
    choices=DUSTLEVEL,
    default=DUSTLEVEL[0][0]
    )
  
  class Meta:
    ordering = ['-date']
  
  # models.CASCADE ensures that all of the child Dustings will be automatically deleted if a Yarn is deleted
  yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)

  def __str__(self):
    # Django has automatically created the display method to access the value of dust (Field.choice)
    return f"{self.get_dust_display()} on {self.date}"
  