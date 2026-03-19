from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# ==============================
# TIPOS DE NEGÓCIO (NOVO)
# ==============================
class BusinessType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==============================
# CLIENTES / LEADS (HOUSE)
# ==============================

class House(models.Model):

    TYPE_CHOICES = [
        ("base", "Base"),
        ("client", "Cliente"),
    ]

    STATUS_CHOICES = [
        ("none", "Nenhum"),
        ("new", "Novo"),
        ("not_visited", "Não visitado"),
        ("visited", "Visitado"),
        ("interested", "Interessado"),
        ("not_interested", "Não interessado"),
        ("revisit", "Visitar novamente"),
        ("lead", "Lead"),
        ("contract", "Contrato fechado"),
        ("client", "Cliente"),
        ("past_client", "Já comprou"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="houses",
        null=True,
        blank=True
    )

    # ✅ RELACIONAMENTO DEFINITIVO
    business_type = models.ForeignKey(
        BusinessType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="houses"
    )

    # Identificação
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(null=True, blank=True)

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    whatsapp = models.CharField(max_length=30, blank=True, null=True)

    # Geolocalização
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.PositiveIntegerField(default=500)

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default="base"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="none"
    )

    visits = models.PositiveIntegerField(default=0)

    registered_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def has_active_contract(self):
        return self.contracts.filter(status="active").exists()

    def __str__(self):
        return self.name


# ==============================
# CONTRATOS
# ==============================

class Contract(models.Model):

    STATUS_CHOICES = [
        ("active", "Ativo"),
        ("paused", "Pausado"),
        ("finished", "Finalizado"),
        ("canceled", "Cancelado"),
    ]

    client = models.ForeignKey(
        House,
        related_name="contracts",
        on_delete=models.CASCADE
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def total_value(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"Contrato #{self.id} - {self.client.name}"


# ==============================
# ITENS DO CONTRATO
# ==============================

class ContractItem(models.Model):

    contract = models.ForeignKey(
        Contract,
        related_name="items",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def unit_price(self):
        if self.product.type == "product":
            return self.product.price
        return self.product.monthly_price

    def total_price(self):
        if self.product.type == "product":
            return self.product.price * self.quantity
        return self.product.monthly_price

    def __str__(self):
        return f"{self.product.name} (Contrato {self.contract.id})"
