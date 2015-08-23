# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloga', '0003_post_irudi_nagusia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='irudi_nagusia',
            field=models.ImageField(upload_to=b''),
        ),
    ]
