# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 4.2.11 on 2024-05-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("security", "0006_auto_20200122_0957"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mitrecve",
            name="order",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="mitrecve",
            name="year",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="securityadvisory",
            name="order",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="securityadvisory",
            name="year",
            field=models.IntegerField(),
        ),
    ]
