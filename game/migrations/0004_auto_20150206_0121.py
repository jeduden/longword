# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_wordsubmission_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordsubmission',
            old_name='date',
            new_name='submitted',
        ),
    ]
