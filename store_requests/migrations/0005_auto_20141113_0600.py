# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_requests', '0004_store_request_request_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_request',
            name='rent_price',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
