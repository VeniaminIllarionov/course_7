# Generated by Django 4.2 on 2024-07-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habits_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='is_publish',
            field=models.CharField(choices=[(True, 'Опубликовано'), (False, 'Не опубликовано')], default=False, max_length=80, verbose_name='Признак публичности'),
        ),
    ]
