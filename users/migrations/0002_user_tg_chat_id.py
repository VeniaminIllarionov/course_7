# Generated by Django 4.2 on 2024-07-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_chat_id',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Телеграмм id'),
        ),
    ]
