# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogentry', '0004_taggeditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggeditem',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='TaggedItem',
        ),
    ]
