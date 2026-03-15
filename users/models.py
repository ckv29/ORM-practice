from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя с дополнительными полями
    """
    # email делаем уникальным и обязательным
    email = models.EmailField(_('email address'), unique=True)

    # Дополнительные поля
    bio = models.TextField(_('biography'), max_length=500, blank=True, help_text="Расскажите немного о себе")
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    #avatar = models.ImageField(_('avatar'), upload_to='avatars/', null=True, blank=True)

    # Дополнительные метаданные
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
