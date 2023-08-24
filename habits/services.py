from django_celery_beat.models import CrontabSchedule, PeriodicTask


def set_schedule(habit):
    schedule, created = CrontabSchedule.objects.get_or_create(
            minute=habit.starting_time.minute,
            hour=habit.starting_time.hour,
            day_of_month=f'*/{habit.interval}',
            month_of_year='*',
            day_of_week='*',
        )

    PeriodicTask.objects.create(
        crontab=schedule,
        name=f'Habit Task - {habit.action}',
        task='habits.tasks.habits_notification',
        args=[habit.id],
    )
