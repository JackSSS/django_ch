# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150803_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='motionrange',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'none'), (1, b'minimal'), (2, b'some'), (3, b'ample')]),
        ),
        migrations.AlterField(
            model_name='robot',
            name='payload',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'none'), (1, b'minimal'), (2, b'some'), (3, b'ample')]),
        ),
    ]
