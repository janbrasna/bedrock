# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 4.2.16 on 2024-09-30 14:40

import django.db.models.deletion
from django.db import migrations, models

import wagtail.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0093_uploadedfile"),
        ("cms", "0002_bedrockimage_bedrockrendition"),
    ]

    operations = [
        migrations.CreateModel(
            name="VPNCallToActionSnippet",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("heading", models.CharField(max_length=255)),
                (
                    "image",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="cms.bedrockimage"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VPNResourceCenterIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("sub_title", models.CharField(blank=True, max_length=255)),
                (
                    "call_to_action_bottom",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="products.vpncalltoactionsnippet"
                    ),
                ),
                (
                    "call_to_action_middle",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="products.vpncalltoactionsnippet"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="VPNResourceCenterDetailPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("desc", models.CharField(blank=True, help_text="A short description used on index page.", max_length=500)),
                ("content", wagtail.fields.RichTextField(blank=True)),
                (
                    "call_to_action_bottom",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="products.vpncalltoactionsnippet"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="cms.bedrockimage"),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]