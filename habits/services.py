import requests

from config import settings
from habits.models import Habit


def get_habit_message(user):
    habits = Habit.objects.filter(owner=user)
    bonus = None
    for habit in habits:
        useful_habit = habit.action
        if habit.related_habit:
            bonus = habit.related_habit
        elif habit.reward:
            bonus = habit.reward

        message = (
            f"Вам необходимо {useful_habit} в {habit.place}. За это Вы можете {bonus}."
        )

        return message


def send_telegram_message(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.post(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        params=params,
    )
