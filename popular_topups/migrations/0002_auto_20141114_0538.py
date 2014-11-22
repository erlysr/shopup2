# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20141114_0421'),
        ('popular_topups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popular_topup',
            name='store',
        ),
        migrations.AddField(
            model_name='popular_topup',
            name='store_n',
            field=models.ManyToManyField(to='stores.Store'),
            preserve_default=True,
        ),
    ]
