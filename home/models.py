from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_ckeditor_5.fields import CKEditor5Field # type: ignore
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
    image = models.ImageField(upload_to='portfolio/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    message = models.TextField()
    

    def __str__(self):
        return self.naem


class Client(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='Client/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=55)
    user = models.CharField(max_length=55, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='review/')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title


class LatestProject(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='Latest_Project/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Chooseus(models.Model):
    title = models.CharField(max_length=55)
    description = CKEditor5Field('Description', config_name='default')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Gallary(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='gallary/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title