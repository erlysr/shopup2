# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20141114_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='date_approved',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
