# Generated by Django 2.2.15 on 2020-08-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
