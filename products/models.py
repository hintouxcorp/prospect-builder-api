from django.db import models

class Product(models.Model):

    TYPE_CHOICES = [
        ("product", "Produto"),
        ("service", "Serviço"),
    ]

    name = models.CharField(max_length=150)

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    # Produto
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Serviço
    monthly_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
