# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150410_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='number',
            field=models.PositiveIntegerField(unique=True),
            preserve_default=True,
        ),
    ]
