# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gertaerak', '0002_auto_20150820_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gertaera',
            name='mota',
            field=models.ForeignKey(to='gertaerak.GertaeraMota'),
        ),
    ]
