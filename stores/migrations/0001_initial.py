# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tabulators', '__first__'),
        ('addresses', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '__first__'),
        ('status_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=255)),
                ('activity', models.CharField(max_length=255)),
                ('dimentions_width', models.FloatField()),
                ('dimentions_length', models.FloatField()),
                ('store_phone', models.CharField(max_length=12)),
                ('image1', models.ImageField(upload_to=b'stores')),
                ('image2', models.ImageField(upload_to=b'stores', blank=True)),
                ('image3', models.ImageField(upload_to=b'stores', blank=True)),
                ('image4', models.ImageField(upload_to=b'stores', blank=True)),
                ('image5', models.ImageField(upload_to=b'stores', blank=True)),
                ('website', models.CharField(max_length=255, blank=True)),
                ('facebook', models.CharField(max_length=255, blank=True)),
                ('twitter', models.CharField(max_length=255, blank=True)),
                ('youtube', models.CharField(max_length=255, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_approved', models.DateField(blank=True)),
                ('wireless', models.BooleanField(default=False)),
                ('stands', models.BooleanField(default=False)),
                ('repisas', models.BooleanField(default=False)),
                ('boards', models.BooleanField(default=False)),
                ('lighting', models.BooleanField(default=False)),
                ('electricity', models.BooleanField(default=False)),
                ('water', models.BooleanField(default=False)),
                ('airconditioning', models.BooleanField(default=False)),
                ('toilets', models.BooleanField(default=False)),
                ('heating', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('parkinglot', models.BooleanField(default=False)),
                ('counter', models.BooleanField(default=False)),
                ('phoneline', models.BooleanField(default=False)),
                ('storehouse', models.BooleanField(default=False)),
                ('dressingroom', models.BooleanField(default=False)),
                ('others1', models.BooleanField(default=False)),
                ('others2', models.BooleanField(default=False)),
                ('others3', models.BooleanField(default=False)),
                ('price', models.FloatField(blank=True)),
                ('address', models.ForeignKey(to='addresses.Address')),
                ('contact', models.ForeignKey(to='contacts.Contact')),
                ('status', models.ForeignKey(to='status_types.Status_Type')),
                ('tabulator', models.ForeignKey(to='tabulators.Tabulator')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
