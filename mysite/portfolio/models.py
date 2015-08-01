from django.db import models
import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField
    authors = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Map(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    authors = models.CharField(max_length=300)
    project = models.ForeignKey(Project)
    image = models.ImageField(upload_to='maps')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=200)
    citation = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title



