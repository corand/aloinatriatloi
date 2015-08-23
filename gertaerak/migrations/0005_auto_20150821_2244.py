# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gertaerak', '0004_gertaera_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gertaera',
            name='textua',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
