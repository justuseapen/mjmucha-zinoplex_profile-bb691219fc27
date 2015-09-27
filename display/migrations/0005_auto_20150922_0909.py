# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_auto_20150919_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
        migrations.AddField(
            model_name='ppi_scorecard',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ppi_scorecard',
            name='index_a',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ppi_scorecard',
            name='index_b',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ppi_scorecard',
            name='index_c',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ppi_scorecard',
            name='index_d',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='degree',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='honor',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ppi_scorecard',
            name='index_e',
            field=models.IntegerField(default=0),
        ),
    ]
