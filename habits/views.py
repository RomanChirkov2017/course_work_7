from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import MyPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListAPIView(ListAPIView):
    """Контроллер просмотра списка публичных привычек."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Habit.objects.filter(is_public=True)
        return queryset


class UserHabitListAPIView(ListAPIView):
    """Контроллер просмотра списка привычек пользователя."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = MyPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habit.objects.filter(owner=user)
        else:
            queryset = Habit.objects.all()
        return queryset


class HabitCreateAPIView(CreateAPIView):
    """Контроллер создания привычки."""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    """Контроллер для детального просмотра одной привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class HabitUpdateAPIView(UpdateAPIView):
    """Контроллер для редактирования привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """Контроллер для удаления привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
