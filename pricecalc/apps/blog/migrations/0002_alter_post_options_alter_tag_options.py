# Generated by Django 4.1.2 on 2022-10-06 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-date_pub"],
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={
                "ordering": ["title"],
                "verbose_name": "Тэг к статье",
                "verbose_name_plural": "Тэги к статьм",
            },
        ),
    ]