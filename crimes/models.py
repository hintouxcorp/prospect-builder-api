from django.db import models

class CrimePoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    category = models.CharField(max_length=100)
    severity = models.FloatField(default=1)

    occurred_at = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
