# Generated by Django 3.1.2 on 2020-10-06 19:16

import uuid

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('release_date', models.DateTimeField()),
                ('cost', models.IntegerField(default=0)),
                ('total_listens', models.IntegerField(default=0)),
                ('artwork', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), size=None)),
                ('bandcamp_link', models.CharField(blank=True, max_length=150, null=True)),
                ('beatport_link', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
