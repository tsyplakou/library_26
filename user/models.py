from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        READER = 'reader', _('Reader')
        LIBRARIAN = 'librarian', _('Librarian')

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.READER,
    )
