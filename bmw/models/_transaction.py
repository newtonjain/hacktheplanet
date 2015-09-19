from django.db import models

from bmw.generics import ArchivableModel
from ._driver import Driver
from ._customer import Customer


class Transaction(ArchivableModel):
    price = models.BigIntegerField()
    # relationships
    driver = models.ForeignKey(Driver)
    customer = models.ForeignKey(Customer)
