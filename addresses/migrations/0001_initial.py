# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postal_codes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line1', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('postal_code', models.ForeignKey(to='postal_codes.Postal_Code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
