# Generated by Django 2.2.15 on 2020-08-24 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20200824_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artists',
        ),
    ]
