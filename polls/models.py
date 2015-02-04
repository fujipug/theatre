from django.db import models
from decimal import Decimal

class Performance(models.Model):
    name=models.TextField()
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=5) #military time please
    description=models.TextField(default="Description missing.")
    price=models.DecimalField(default=Decimal(00.00), max_digits=4, decimal_places=2)
    picture=models.TextField()
    def __unicode__(self):
        return self.name

class Movie(models.Model):
    name=models.TextField()
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=5) #military time please
    description=models.TextField(default="Description missing.")
    price=models.DecimalField(default=Decimal(00.00), max_digits=4, decimal_places=2)
    picture=models.TextField()
    def __unicode__(self):
        return self.name
