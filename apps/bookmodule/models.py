from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)


class Address(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField(default=18)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Address2(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Student2(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField(default=18)
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name

class Images(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images/')