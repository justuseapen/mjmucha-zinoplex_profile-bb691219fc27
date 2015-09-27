# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture_url',
            field=models.CharField(max_length=150, blank=True, default='/static/Person-icon-grey.jpg', null=True),
        ),
    ]
