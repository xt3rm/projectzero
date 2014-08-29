from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    
    
class Entry(models.Model):
    title  = models.CharField(max_length=50)
    blog   = models.ForeignKey(Blog)
    text   = models.CharField(max_length=4000)
    date   = models-DateTimeField('date published')
    author = models.ForeignKey(Author)




