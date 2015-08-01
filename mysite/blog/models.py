from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100)
    content = models.TextField()
    short = models.TextField()
    tags = models.CharField(max_length=200, default='All')

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField()
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.title

class BlogCitation(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    work = models.CharField(max_length=200)
    pages = models.CharField(max_length=50)
    date = models.DateTimeField('date')
    link = models.CharField(max_length=300, default='No Link')
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.title
