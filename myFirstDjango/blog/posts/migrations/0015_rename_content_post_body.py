# Generated by Django 4.2.9 on 2024-02-18 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0014_alter_post_content"),
    ]

    operations = [
        migrations.RenameField(model_name="post", old_name="content", new_name="body",),
    ]