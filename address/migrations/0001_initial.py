# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
    ]
