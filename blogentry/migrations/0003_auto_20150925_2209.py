# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogentry', '0002_auto_20150925_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentry',
            options={'ordering': ['-published_date']},
        ),
        migrations.AddField(
            model_name='blogentry',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
