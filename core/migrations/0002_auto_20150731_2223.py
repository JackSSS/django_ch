# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='axes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='h_reach',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='mass',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='motion_range',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='motion_speed',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='payload',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='repeatability',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='structure',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='v_reach',
            field=models.TextField(null=True, blank=True),
        ),
    ]
