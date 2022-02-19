# Generated by Django 4.0.2 on 2022-02-07 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calc_title', models.CharField(max_length=30, verbose_name='название калькулятора')),
                ('calc_text', models.TextField(verbose_name='текст кальк')),
                ('calc_date', models.DateTimeField(verbose_name='дата рассчёта')),
            ],
            options={
                'verbose_name': 'Калькуль',
                'verbose_name_plural': 'Калькули',
            },
        ),
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_title', models.CharField(max_length=50, verbose_name='price_title')),
                ('price_date', models.DateTimeField(verbose_name='price_date')),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='user_name')),
            ],
        ),
        migrations.CreateModel(
            name='SpecificationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.calculation')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='calc.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('det_heigth', models.IntegerField(verbose_name='det_higth')),
                ('det_widht', models.IntegerField(verbose_name='det_widht')),
                ('det_material', models.TextField(verbose_name='det_material')),
                ('specdetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.specificationdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='name avtor')),
                ('comment_text', models.CharField(max_length=50, verbose_name='текст комм')),
                ('calc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.calc')),
            ],
            options={
                'verbose_name': 'комент',
                'verbose_name_plural': 'коменты',
            },
        ),
        migrations.AddField(
            model_name='calculation',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='calculs', to='calc.Tag'),
        ),
        migrations.AddField(
            model_name='calculation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.user'),
        ),
    ]
