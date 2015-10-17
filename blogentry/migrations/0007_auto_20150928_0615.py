# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogentry', '0006_blogentry_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogentry',
            name='likes',
        ),
        migrations.AddField(
            model_name='likes',
            name='title',
            field=models.ForeignKey(to='blogentry.BlogEntry'),
        ),
    ]
