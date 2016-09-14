# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-14 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('a_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mig_error.A')),
            ],
            bases=('mig_error.a',),
        ),
    ]
