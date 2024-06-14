from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import get_habit_message, send_telegram_message


@shared_task
def send_tg_notification():
    current_datetime = timezone.now().today().replace(second=0, microsecond=0)
    habits = Habit.objects.filter(time=current_datetime).filter(is_pleasant=False)

    for habit in habits:
        user = habit.owner
        message = get_habit_message(user)
        send_telegram_message(user.telegram_chat_id, message)
        habit.time = habit.time + timedelta(days=habit.periodicity)
        habit.save()
