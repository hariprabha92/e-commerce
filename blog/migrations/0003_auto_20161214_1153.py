# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-14 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='product_description',
        ),
    ]
