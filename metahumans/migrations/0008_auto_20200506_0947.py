# Generated by Django 3.0.5 on 2020-05-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0007_auto_20200505_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metahuman',
            options={'verbose_name': 'Metahumano', 'verbose_name_plural': 'Metahumanos'},
        ),
        migrations.AlterModelOptions(
            name='power',
            options={'verbose_name': 'Poder', 'verbose_name_plural': 'Poderes'},
        ),
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True),
        ),
    ]