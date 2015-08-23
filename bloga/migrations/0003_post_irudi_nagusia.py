# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloga', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='irudi_nagusia',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
