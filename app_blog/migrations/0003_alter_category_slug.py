# Generated by Django 4.0.2 on 2022-04-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_category_options_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Слаг'),
        ),
    ]
