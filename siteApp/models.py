from django.db import models

# Create your models here.


class Site(models.Model):
    nom = models.CharField(max_length=50)
    sectionImageblock= models.FileField( upload_to="site_imgs", )
    sectionBlockLabele =models.CharField(max_length=100)
    menuDescription = models.TextField()
    sectionNewsLetter = models.CharField( max_length=100)
    adresse = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    sectionDescription = models.TextField()
    sectionCopyright =models.CharField(max_length=50)
    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)

class Banner(models.Model):
    image_banners = models.FileField( upload_to="banner_imgs")
    
    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)
    

class Contact(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField() 

    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)

class Reseau_social(models.Model):
    icon = models.CharField( max_length=50)
    nom = models.CharField( max_length=50)
    link = models.CharField( max_length=255)

    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)

class Newsletter(models.Model):
    email = models.EmailField( max_length=254) 

    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)