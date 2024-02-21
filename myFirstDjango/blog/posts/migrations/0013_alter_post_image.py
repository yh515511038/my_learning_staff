# Generated by Django 5.0.1 on 2024-02-16 04:22

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0012_alter_tag_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=imagekit.models.fields.ProcessedImageField(
                null=True, upload_to="posts"
            ),
        ),
    ]