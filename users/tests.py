from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@mail.com",
            password="12345"
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тест создания пользователя."""
        url = reverse("users:register")
        data = {"email": "test_test@yandex.ru", "password": "54321"}

        response = self.client.post(url, data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("email"), "test_test@yandex.ru")
