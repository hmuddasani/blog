# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogentry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='description',
            field=models.TextField(),
        ),
    ]
