# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gertaerak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GertaeraMota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('izena', models.CharField(max_length=100)),
                ('irudia', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='gertaera',
            name='mota',
            field=models.ForeignKey(blank=True, to='gertaerak.GertaeraMota', null=True),
        ),
    ]
