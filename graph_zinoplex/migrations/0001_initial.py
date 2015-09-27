# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GraphNode',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('links', models.ManyToManyField(to='graph_zinoplex.GraphNode', through='graph_zinoplex.GraphLink')),
            ],
        ),
        migrations.CreateModel(
            name='GraphTreeNode',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('type', models.CharField(max_length='10')),
                ('graph_node', models.ForeignKey(to='graph_zinoplex.GraphNode', null=True, blank=True)),
                ('parent', models.ForeignKey(to='graph_zinoplex.GraphTreeNode', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='graphlink',
            name='source',
            field=models.ForeignKey(to='graph_zinoplex.GraphNode', related_name='source'),
        ),
        migrations.AddField(
            model_name='graphlink',
            name='target',
            field=models.ForeignKey(to='graph_zinoplex.GraphNode', related_name='target'),
        ),
    ]
