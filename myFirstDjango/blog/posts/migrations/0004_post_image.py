# Generated by Django 4.2.9 on 2024-02-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_post_posted"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.CharField(default="mountains.jpg", max_length=100),
        ),
    ]