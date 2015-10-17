# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogentry', '0005_auto_20150926_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='likes',
            field=models.ManyToManyField(related_name='like', to='blogentry.BlogEntry'),
        ),
    ]
