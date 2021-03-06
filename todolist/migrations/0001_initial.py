# Generated by Django 3.2 on 2022-04-07 07:16

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
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Дело')),
                ('description', models.TextField(blank=True, verbose_name='Описание дела')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_completed', models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения')),
                ('important', models.BooleanField(default=False, verbose_name='Важность')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто оставил')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
