# Generated by Django 4.0.2 on 2022-03-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0019_alter_furniture_price_retail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('article', models.CharField(default=None, max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=8)),
                ('price_retail', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('availability', models.CharField(default=None, max_length=20)),
            ],
            options={
                'verbose_name': 'Ручка',
                'verbose_name_plural': 'Ручки',
            },
        ),
        migrations.AlterModelOptions(
            name='furniture',
            options={'verbose_name': 'Фурнитура', 'verbose_name_plural': 'Фурнитура'},
        ),
    ]