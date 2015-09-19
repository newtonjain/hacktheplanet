from django.db import models

from address.models import AddressField
from users.models import User

BIKE_MODELS = (
    ('BMW G 650 GS', 'BMW G 650 GS'),
    ('BMW F 700 GS', 'BMW F 700 GS'),
    ('BMW F 800 GS', 'BMW F 800 GS'),
    ('BMW S 1000 XR', 'BMW S 1000 XR'),
)


class Driver(User):
    bike_model = models.CharField(
        max_length=100,
        choices=BIKE_MODELS,
        default='BMW G 650 GS')
    location = AddressField(
        blank=True,
        null=True)
