# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160113_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreEntidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Diagramax',
            new_name='Diagramas',
        ),
    ]
