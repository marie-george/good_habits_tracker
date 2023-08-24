from celery import shared_task
from django.core.mail import send_mail
from telebot import TeleBot

from config import settings
from habits.models import Habit


@shared_task
def habits_notification(object_pk):
    habit = Habit.objects.get(pk=object_pk)
    # send_mail(
    #     subject='Напоминание о привычке',
    #     message=f'Трекер привычек напоминает: требуется совершить {habit.action}',
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[habit.creator.email]
    # )
    bot = TeleBot(settings.TG_BOT_TOKEN)
    message = f'Трекер привычек напоминает: требуется совершить {habit.action} в {habit.starting_time} в {habit.place}'
    print(message)
    bot.send_message(habit.creator.chat_id, message)