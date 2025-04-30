from django.db import models

# Create your models here.

class Banar(models.Model):
    title = models.CharField(max_length=55)
    short_description = models.CharField(max_length=55)
    banar_image = models.ImageField(upload_to='bannar/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='Service/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='Service/')
    price = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.Name
    

class Portfolio(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='Service/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

