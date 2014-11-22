# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent_types', '__first__'),
        ('status_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store_Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('rent_price', models.FloatField(blank=True)),
                ('start_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('rent_type', models.ForeignKey(to='rent_types.Rent_Type')),
                ('status_req', models.ForeignKey(to='status_types.Status_Type')),
                ('store', models.ForeignKey(to='stores.Store')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
