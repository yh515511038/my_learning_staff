# Generated by Django 4.2.9 on 2024-02-09 08:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_post_tag"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="tag",),
        migrations.AddField(
            model_name="post",
            name="excerpt",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                null=True, related_name="posts", to="posts.tag"
            ),
        ),
        migrations.AlterField(
            model_name="author", name="email", field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="posts.author",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(
                validators=[django.core.validators.MinLengthValidator(10)]
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, default="", unique=True),
        ),
        migrations.AlterField(
            model_name="tag", name="caption", field=models.CharField(max_length=20),
        ),
    ]
