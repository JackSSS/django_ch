# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150731_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='h_reach',
        ),
        migrations.RemoveField(
            model_name='robot',
            name='motion_range',
        ),
        migrations.RemoveField(
            model_name='robot',
            name='motion_speed',
        ),
        migrations.RemoveField(
            model_name='robot',
            name='v_reach',
        ),
        migrations.AddField(
            model_name='robot',
            name='hreach',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'weak'), (2, b'fair'), (3, b'standard'), (4, b'strong'), (5, b'exclusive')]),
        ),
        migrations.AddField(
            model_name='robot',
            name='motionrange',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AddField(
            model_name='robot',
            name='speed',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'constant speed'), (1, b'can accelerate')]),
        ),
        migrations.AddField(
            model_name='robot',
            name='vreach',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'weak'), (2, b'fair'), (3, b'standard'), (4, b'strong'), (5, b'exclusive')]),
        ),
        migrations.AlterField(
            model_name='robot',
            name='axes',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'1'), (1, b'2'), (2, b'3'), (3, b'4'), (4, b'5'), (5, b'6+')]),
        ),
        migrations.AlterField(
            model_name='robot',
            name='mass',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'1'), (1, b'2'), (2, b'3'), (3, b'4'), (4, b'5'), (5, b'6+')]),
        ),
        migrations.AlterField(
            model_name='robot',
            name='payload',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AlterField(
            model_name='robot',
            name='repeatability',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='robot',
            name='structure',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'weak'), (2, b'fair'), (3, b'standard'), (4, b'strong'), (5, b'exclusive')]),
        ),
    ]
