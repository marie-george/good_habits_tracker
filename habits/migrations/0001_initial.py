# Generated by Django 4.2.4 on 2023-08-23 20:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=500, verbose_name='действие')),
                ('place', models.CharField(max_length=150, verbose_name='место')),
                ('starting_time', models.TimeField(verbose_name='время начала')),
                ('execution_time', models.IntegerField(validators=[django.core.validators.MaxValueValidator(120)], verbose_name='время на выполнение в сек.')),
                ('interval', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(7)], verbose_name='периодичность выполнения - один раз в ... дней')),
                ('reward', models.CharField(blank=True, max_length=500, null=True, verbose_name='вознаграждение')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('bound_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связанная привычка')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель привычки')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('action',),
            },
        ),
    ]
