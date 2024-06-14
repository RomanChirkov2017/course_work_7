from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="test@mail.com", password="12345")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place="на улице",
            time="2024-06-15 08:00:00",
            action="выйти на пробежку",
            is_pleasant=False,
            periodicity=1,
            reward="съесть фрукт",
            time_to_complete=100,
            is_public=True,
            related_habit=None,
        )

    def test_habit_create(self):
        """Тест создания привычки."""
        url = reverse("habits:habits_create")
        data = {
            "owner": self.user.id,
            "place": "дома",
            "time": "2024-06-15 20:00:00",
            "action": "сделать отжимания",
            "is_pleasant": "False",
            "periodicity": 1,
            "reward": "выпить свежевыжатый сок",
            "time_to_complete": 90,
            "is_public": "True",
        }
        response = self.client.post(url, data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_user_habits_list(self):
        """Тест получения списка привычек пользователя."""
        url = reverse("habits:user_habits_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_retrieve(self):
        """Тест просмотра одной конкретной привычки."""
        url = reverse("habits:habits_detail", kwargs={"pk": self.habit.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        """Тест изменения привычки."""
        url = reverse("habits:habits_update", kwargs={"pk": self.habit.id})
        data = {
            "reward": "съесть апельсин",
        }
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habits_list(self):
        """Тест получения списка всех привычек."""
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        """Тест удаления привычки."""
        url = reverse("habits:habits_delete", kwargs={"pk": self.habit.id})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
