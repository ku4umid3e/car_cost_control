from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1)
    fuel_tank_volume = models.IntegerField()
    mileage = models.IntegerField()
