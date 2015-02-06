# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20150206_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordsubmission',
            name='submitted',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
