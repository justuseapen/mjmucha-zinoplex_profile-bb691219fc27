# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20150919_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
