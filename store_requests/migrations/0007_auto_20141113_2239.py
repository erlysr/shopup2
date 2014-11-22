# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_requests', '0006_auto_20141113_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_request',
            name='rent_price',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
