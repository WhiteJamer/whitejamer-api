from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    is_private = models.BooleanField(default=False, help_text="Hide profile information?")
