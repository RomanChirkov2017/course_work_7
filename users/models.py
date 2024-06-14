from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите почту"
    )

    first_name = models.CharField(max_length=150, verbose_name="Имя", **NULLABLE)
    last_name = models.CharField(max_length=200, verbose_name="Фамилия", **NULLABLE)
    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Укажите телефон",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )
    city = models.CharField(
        max_length=150, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )
    telegram_chat_id = models.CharField(
        max_length=100, unique=True, verbose_name="Telegram_chat_id", **NULLABLE
    )
    verification_token = models.CharField(
        max_length=50, verbose_name="Код верификации", **NULLABLE
    )
    last_login = models.DateTimeField(**NULLABLE, verbose_name="Дата последнего входа")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
