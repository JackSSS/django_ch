# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150802_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robot',
            old_name='axes',
            new_name='axles',
        ),
    ]
