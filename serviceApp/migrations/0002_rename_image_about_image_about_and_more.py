# Generated by Django 4.0.4 on 2022-05-17 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image',
            new_name='image_about',
        ),
        migrations.RenameField(
            model_name='platfavorie',
            old_name='image',
            new_name='image_plat_favori',
        ),
    ]
