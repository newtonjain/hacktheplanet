from django.db import models

from bmw.generics import ArchivableModel
from ._driver import Driver


class Transaction(ArchivableModel):
    price = models.BigIntegerField()
    # relationships
    driver = models.ForeignKey(Driver)
