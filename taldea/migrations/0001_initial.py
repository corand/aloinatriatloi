# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Harremana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('izena', models.CharField(max_length=150)),
                ('emaila', models.EmailField(max_length=254)),
                ('textua', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
