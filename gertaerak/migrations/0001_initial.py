# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gertaera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('izena', models.CharField(max_length=100)),
                ('textua', models.TextField()),
                ('kokapena', geoposition.fields.GeopositionField(max_length=42)),
                ('helbidea', models.CharField(max_length=100)),
                ('ordua', models.DateTimeField()),
                ('weba', models.URLField()),
            ],
        ),
    ]
