from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "is_pleasant",
        "periodicity",
        "time_to_complete",
        "is_public",
    )
    list_filter = (
        "id",
        "owner",
        "is_pleasant",
        "is_public",
    )
