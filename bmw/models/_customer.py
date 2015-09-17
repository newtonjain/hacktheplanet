from django.db import models

from users.models import User


class Driver(User):
    driver_field = models.CharField(max_length=100)
