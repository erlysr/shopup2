# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_requests', '0002_auto_20141113_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_request',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
