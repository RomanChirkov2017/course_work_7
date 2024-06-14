from datetime import timedelta

from rest_framework.serializers import ValidationError


class TimeToCompleteValidator:
    """Время выполнения не должно превышать 120 секунд."""

    def __call__(self, value):
        if value:
            if timedelta(seconds=value) > timedelta(seconds=120):
                raise ValidationError(
                    "Время на выполнение не должно превышать 120 секунд."
                )


class PeriodicityValidator:
    """Периодичность выполнения привычки должна быть не реже 1 раза в 7 дней."""

    def __call__(self, value):
        if value:
            if not 1 <= value <= 7:
                raise ValidationError(
                    "Периодичность выполнения привычки должна быть не реже 1 раза в 7 дней."
                )


class PleasantHabitValidator:
    """Приятная привычка не может иметь связанной привычки или вознаграждения."""

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        if value.get(self.field1) and (
            value.get(self.field2) or value.get(self.field3)
        ):
            raise ValidationError(
                "Приятная привычка не может иметь связанной привычки или вознаграждения."
            )


class RewardOrPleasantHabitValidator:
    """У полезной привычки не может быть одновременно и приятной привычки, и вознаграждения."""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if value.get(self.field1) and value.get(self.field2):
            raise ValidationError(
                "У полезной привычки не может быть одновременно и приятной привычки, и вознаграждения."
            )


class RelatedHabitValidator:
    """Связанной привычкой может быть только приятная привычка."""

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        if value.get(self.field1):
            if not value.get(self.field1).is_pleasant:
                raise ValidationError(
                    "Связанной привычкой может быть только приятная привычка."
                )
