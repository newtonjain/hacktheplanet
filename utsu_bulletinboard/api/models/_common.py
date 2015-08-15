from django.db import models


class Location(models.Model):
	x = models.DecimalField(max_digits=10, decimal_places=6)
	y = models.DecimalField(max_digits=10, decimal_places=6)
	