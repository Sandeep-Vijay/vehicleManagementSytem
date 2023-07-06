from django.db import models

class Vms(models.Model):
    carname=models.CharField(max_length=150)
    fueltype=models.CharField(max_length=150)
    carnumber=models.CharField(max_length=150)
    model=models.CharField(max_length=150)

    def __str__(self):
        return self.carname