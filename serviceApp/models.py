from django.db import models

# Create your models here.

class PlatFavorie(models.Model):
    nom =models.CharField( max_length=50)
    image_plat_favori = models.FileField(upload_to="plat_img") 
    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)

class About(models.Model):
    image_about=models.FileField( upload_to="about_img")
    libele = models.CharField( max_length=50)
    description = models.TextField() 
    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)

class Blog(models.Model):
    image_blog = models.FileField(upload_to="blog_img")
    nom = models.CharField(max_length=50)
    description = models.TextField()
    date_update = models.DateTimeField( auto_now=True)
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)


class Menu(models.Model):
    nomPlat = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.TextField()
    date_update = models.DateTimeField( )
    date_add = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField( default=True)
    