from celery import shared_task
from django.core.mail import send_mail
from telebot import TeleBot

from config import settings
from habits.models import Habit


@shared_task
def habits_notification(object_pk):
    habit = Habit.objects.get(pk=object_pk)
    bot = TeleBot(settings.TG_BOT_TOKEN)
    message = f'Трекер привычек напоминает: требуется совершить {habit.action} в {habit.starting_time} в {habit.place}'
    print(message)
    bot.send_message(habit.creator.chat_id, message)