from rest_framework import serializers

from habits.models import Habit
from habits.validators import (PeriodicityValidator, PleasantHabitValidator,
                               RelatedHabitValidator,
                               RewardOrPleasantHabitValidator,
                               TimeToCompleteValidator)


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[TimeToCompleteValidator()])
    periodicity = serializers.IntegerField(validators=[PeriodicityValidator()])

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            PleasantHabitValidator(
                field1="is_pleasant", field2="reward", field3="related_habit"
            ),
            RewardOrPleasantHabitValidator(field1="reward", field2="related_habit"),
            RelatedHabitValidator(field1="related_habit"),
        ]
