# Generated by Django 5.0.6 on 2024-05-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_alter_image_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='images',
        ),
    ]