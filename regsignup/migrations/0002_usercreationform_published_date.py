# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regsignup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreationform',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]