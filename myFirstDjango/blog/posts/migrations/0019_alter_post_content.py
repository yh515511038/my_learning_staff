# Generated by Django 5.0.1 on 2024-02-25 03:17

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0018_remove_post_body_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=django_ckeditor_5.fields.CKEditor5Field(
                default="", verbose_name="Text"
            ),
        ),
    ]
