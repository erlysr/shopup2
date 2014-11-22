# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20141117_2324'),
        ('towns', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Byzone_Topup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone_name', models.CharField(max_length=255)),
                ('priority', models.PositiveIntegerField()),
                ('store', models.ManyToManyField(to='stores.Store')),
                ('town', models.ForeignKey(to='towns.Town')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
