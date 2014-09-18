from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class Entry(models.Model):
    title = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog)
    text = models.CharField(max_length=4000)
    date = models.DateTimeField('date published')
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.text



