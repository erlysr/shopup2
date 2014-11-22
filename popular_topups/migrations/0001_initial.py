# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topups', '__first__'),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_Topup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField()),
                ('store', models.ForeignKey(to='stores.Store')),
                ('topup', models.ForeignKey(to='topups.Topup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
