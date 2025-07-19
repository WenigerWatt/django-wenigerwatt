from django.db import models


class YearlyUsage(models.Model):
    year = models.IntegerField(unique=True)
    energy_mwh = models.FloatField()

    def __str__(self):
        return f"{self.year}: {self.energy_mwh} MWh"

class MonthlyUsage(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    consumption = models.FloatField()

    class Meta:
        unique_together = ('year', 'month')
        ordering = ['year', 'month']

    def __str__(self):
        return f"{self.year}-{self.month:02d}: {self.consumption} Durchschnittlicher Verbrauch in 15 Minuten"
