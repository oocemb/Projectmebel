# Generated by Django 4.0.2 on 2022-03-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0017_alter_furniture_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='price_retail',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=8, null=True),
        ),
    ]
