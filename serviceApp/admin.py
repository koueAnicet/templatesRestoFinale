from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import * #PlatFavorie,About,About,
# Register your models here.




@admin.register(PlatFavorie)
class PlatFavorieAdmin(admin.ModelAdmin):

    list_display = ('image', 'image_plat_favori', 'date_update', 'date_add', 'status')
    search_fields = ['nom']
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.image_plat_favori.url}" style="height:100px; width:200px">')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ('image', 'libele', 'description', 'date_update', 'date_add', 'status')
    search_fields = ['libele',]
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.image_about.url}" style="height:100px; width:200px">')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('image', 'nom', 'description', 'date_update', 'date_add', 'status')
    search_fields = ['nom']
    
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.image_blog.url}" style="height:100px; width:200px">')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('nomPlat', 'prix', 'description', 'date_update', 'date_add', 'status')
    search_fields = ['nomPlat']



