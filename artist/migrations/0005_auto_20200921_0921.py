# Generated by Django 2.2.15 on 2020-09-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0004_artist_albums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='albums',
            field=models.ManyToManyField(blank=True, to='album.Album'),
        ),
    ]
