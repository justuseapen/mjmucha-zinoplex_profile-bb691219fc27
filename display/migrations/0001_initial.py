# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graph_zinoplex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('logo_url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PPI_scorecard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('index_e', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('title', models.CharField(null=True, blank=True, max_length=10)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('picture_url', models.URLField(default='/static/Person-icon-grey.jpg')),
                ('linkedin_url', models.URLField(null=True, blank=True)),
                ('graph_node', models.OneToOneField(to='graph_zinoplex.GraphNode')),
                ('user_account', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_started', models.DateField(null=True, blank=True)),
                ('date_ended', models.DateField(null=True, blank=True)),
                ('description', models.TextField()),
                ('company', models.ForeignKey(to='display.Company')),
                ('user_profile', models.ForeignKey(to='display.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='ppi_scorecard',
            name='user_profile',
            field=models.ForeignKey(to='display.Profile'),
        ),
    ]
