from django.db import models
from django.core.validators import MaxValueValidator

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='создатель привычки')
    action = models.CharField(max_length=500, verbose_name='действие') # действие, которое представляет из себя привычка
    place = models.CharField(max_length=150, verbose_name='место')  # место, в котором необходимо выполнять привычку
    starting_time = models.TimeField(verbose_name='время начала') # время, когда необходимо начать выполнять привычку
    execution_time = models.IntegerField(validators=[MaxValueValidator(120)], verbose_name='время на выполнение в сек.') # время, которое предположительно потратит пользователь на выполнение привычки
    interval = models.IntegerField(validators=[MaxValueValidator(7)], default=1, verbose_name='периодичность выполнения - один раз в ... дней') # периодичность выполнения привычки для напоминания в днях
    reward = models.CharField(max_length=500, **NULLABLE, verbose_name='вознаграждение') # чем пользователь должен себя вознаградить после выполнения
    bound_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('action',)

    def __str__(self):
        return self.action

