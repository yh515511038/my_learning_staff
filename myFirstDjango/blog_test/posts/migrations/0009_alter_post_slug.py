# Generated by Django 4.2.9 on 2024-02-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0008_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, default="", editable=False),
        ),
    ]