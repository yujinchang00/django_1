from django.db import models

# Create your models here.

class Blog(models.Model) :
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self) :
        return self.body[:100]

class Song(models.Model) :
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self) :
        return self.title