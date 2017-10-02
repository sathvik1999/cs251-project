# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 03:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='uploaded_at',
            new_name='published_date',
        ),
        migrations.AddField(
            model_name='document',
            name='author',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='document',
            name='genre',
            field=models.CharField(choices=[(b'fi', b'fiction'), (b'fe', b'fear')], default=b'fi', max_length=2),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='document',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
