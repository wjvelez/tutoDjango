# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_categories_customercustomerdemo_customerdemographics_customers_employees_employeeterritories_orderde'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidades2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreEntidad2', models.CharField(max_length=20)),
            ],
        ),
    ]
