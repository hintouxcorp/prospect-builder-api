from django.db import models
from houses.models import House

class ProductSale(models.Model):

    TYPE_CHOICES = [
        ("product", "Produto"),
        ("service", "Serviço"),
    ]

    STATUS_CHOICES = [
        ("active", "Ativo"),
        ("cancelled", "Cancelado"),
    ]

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name="sales"
    )

    name = models.CharField(max_length=150)

    sale_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    # Produto (pagamento único)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Serviço (recorrente)
    monthly_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    start_date = models.DateField(null=True, blank=True)
    cancelled_at = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sale_type})"
