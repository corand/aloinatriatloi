# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gertaerak', '0003_auto_20150821_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='gertaera',
            name='slug',
            field=models.CharField(unique=True, max_length=150, blank=True),
        ),
    ]
