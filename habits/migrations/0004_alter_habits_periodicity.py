# Generated by Django 4.2 on 2024-07-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habits_is_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='periodicity',
            field=models.CharField(choices=[('everyday', 'Ежедневно'), ('every_week', 'Еженедельно')], default='everyday', max_length=80, verbose_name='Периодичность'),
        ),
    ]
