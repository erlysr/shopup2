# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_requests', '0003_auto_20141113_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='store_request',
            name='request_code',
            field=models.CharField(default='R00001', max_length=6),
            preserve_default=False,
        ),
    ]
