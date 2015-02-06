# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordsubmission',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='wordsubmission',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
