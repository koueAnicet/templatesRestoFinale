from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Site
# Register your models here.

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['images_view','nom','sectionBlockLabele', 'menuDescription','sectionNewsLetter','adresse','email','sectionDescription','sectionCopyright','date_update','date_add','status']
    #search_fields = ['nom']
    
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.sectionImageblock.url}" style="height:100px; width:200px">')
    images_view.short_description = 'Aperçu des images' 
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):

    list_display = ['images_view','date_update','date_add','status']
    
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image_banners.url}" style="height:100px; width:200px">')
    images_view.short_description = 'Aperçu des images' 
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('nom','email','message','date_update','date_add','status')
    search_fields = ['nom']
    
@admin.register(Reseau_social)
class Reseau_socialAdmin(admin.ModelAdmin):

    list_display = ('icon','nom','link','date_update','date_add','status')
    search_fields = ['nom']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('email','date_update','date_add','status')
    search_fields = ['email']
   