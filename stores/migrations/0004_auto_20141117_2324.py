# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20141117_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='date_created',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
