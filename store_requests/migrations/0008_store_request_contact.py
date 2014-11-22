# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '__first__'),
        ('store_requests', '0007_auto_20141113_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='store_request',
            name='contact',
            field=models.ForeignKey(default=1, to='contacts.Contact'),
            preserve_default=False,
        ),
    ]
