import csv
from django.core.management.base import BaseCommand
from crimes.models import CrimePoint

class Command(BaseCommand):
    help = "Import crimes from CSV"

    def handle(self, *args, **kwargs):
        with open("crimes.csv", newline="", encoding="utf8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                CrimePoint.objects.create(
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                    weight=float(row.get("weight", 1))
                )

        self.stdout.write(self.style.SUCCESS("Crimes imported"))
