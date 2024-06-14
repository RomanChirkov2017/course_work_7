from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, UserHabitListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habits_list"),
    path("user_habits/", UserHabitListAPIView.as_view(), name="user_habits_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habits_create"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits_detail"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits_update"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habits_delete"),
]
