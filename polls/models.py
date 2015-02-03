from django.db import models

class Performance(models.Model):
    name=models.TextField()
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=5) #military time please
    description=models.TextField(default="Description missing.")
    picture=models.TextField()
    def __unicode__(self):
        return self.name

class Movie(models.Model):
    name=models.TextField()
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=5) #military time please
    description=models.TextField(default="Description missing.")
    picture=models.TextField()
    def __unicode__(self):
        return self.name
