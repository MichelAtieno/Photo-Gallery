# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='article_image',
            field=models.ImageField(default='', upload_to='pictures/'),
        ),
    ]