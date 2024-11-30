from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    #address = models.ForeignKey(to)
class address(models.Model):
    city = models.CharField(max_length=50)