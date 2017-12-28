# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regsignup', '0003_signuppage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email_confirmed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='preconmeth',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='ab@cd.com', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='secret_word',
            field=models.CharField(default='secret', max_length=10),
        ),
    ]