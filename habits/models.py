from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.db import models

from config.settings import AUTH_USER_MODEL
from users.models import NULLABLE

zone = pytz.timezone(settings.TIME_ZONE)
current_datetime = datetime.now(zone)


class Habit(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец"
    )
    place = models.CharField(max_length=150, verbose_name="Место")
    time = models.DateTimeField(default=current_datetime, verbose_name="Время")
    action = models.CharField(max_length=250, verbose_name="Действие")
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    periodicity = models.PositiveIntegerField(
        default=1, verbose_name="Периодичность (в днях)"
    )
    reward = models.CharField(max_length=250, verbose_name="Вознаграждение", **NULLABLE)
    time_to_complete = models.PositiveIntegerField(
        default=timedelta(seconds=120),
        verbose_name="Время на выполнение (в секундах)",
        **NULLABLE,
    )
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("action",)
