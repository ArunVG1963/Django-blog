# Generated by Django 4.2.17 on 2024-12-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_3',
        ),
    ]
