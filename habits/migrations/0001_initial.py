# Generated by Django 4.2 on 2024-07-16 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=50, null=True, verbose_name='Место, в котором необходимо выполнять привычку.')),
                ('time', models.TimeField(max_length=25, verbose_name='Время, когда надо выполнить привычку')),
                ('action', models.CharField(blank=True, max_length=100, null=True, verbose_name='Действие, которое представляет собой привычка.')),
                ('sign_habit', models.CharField(choices=[(True, 'Полезная'), (False, 'Вредная')], max_length=80, verbose_name='Признак приятной привычки')),
                ('periodicity', models.CharField(choices=[('everyday', 'Ежедневно'), ('every_week', 'Еженедельно'), ('every_mounth', 'Еженемесячно')], default='everyday', max_length=80, verbose_name='Периодичность')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вознаграждение')),
                ('time_completed', models.SmallIntegerField(verbose_name='Время на выполнение')),
                ('is_publish', models.CharField(choices=[(True, 'Опубликовано'), (False, 'Не опубликовано')], default=True, max_length=80, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habits', verbose_name='Связанная с другой привычкой')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ['-id'],
            },
        ),
    ]
