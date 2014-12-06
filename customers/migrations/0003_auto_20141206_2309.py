# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20141206_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contactado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
