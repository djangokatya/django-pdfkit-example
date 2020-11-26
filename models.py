from django.db import models

class Holiday(models.Model):
    summary = models.TextField()
    date = models.DateField()

class City(models.Model):
    name = models.CharField(max_length=100)
    holidays = models.ManyToManyField(Holiday)
