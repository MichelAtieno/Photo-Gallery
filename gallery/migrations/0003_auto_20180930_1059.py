# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_image_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='article_image',
            field=models.ImageField(default=True, upload_to='pictures/'),
        ),
    ]
