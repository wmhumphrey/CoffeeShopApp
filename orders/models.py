import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20,blank=True,null=True,help_text="Customer's phone number")
    birth_date = models.DateField(null=True, blank=True)
    points = models.PositiveIntegerField(default=0)
    transactions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name} - ID: {self.id}'

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #: {str(self.id)} - {self.created_at.strftime('%d-%m-%Y %H:%M:%S')}"


# DRINK
SIZE_CHOICES = [
    (1, 'Small'),
    (2, 'Medium'),
    (3, 'Large'),
]
# Type of Drink
class DrinkType(models.Model):
    name = models.CharField("Drink Type",max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

# type of flavor
class Flavor(models.Model):
    name = models.CharField("Flavor", max_length=100)

    def __str__(self):
        return self.name

class Milk(models.Model):
    name = models.CharField("Milk Type", max_length=100)

    def __str__(self):
        return self.name

class Drink(models.Model):
    drink_type = models.ForeignKey(DrinkType, on_delete=models.CASCADE)
    size = models.PositiveIntegerField(choices=SIZE_CHOICES, default=1)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    milk = models.ForeignKey(Milk, on_delete=models.CASCADE)
    extra_shots = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    whip_cream = models.BooleanField(default=False)

    def __str__(self):
        details = f"{self.drink_type.name} ({dict(SIZE_CHOICES).get(self.size)})"
        details += f", {self.flavor.name}"
        details += f", {self.milk.name}"
        if self.extra_shots:
            details += f", Extra Shots: {self.extra_shots}"
        if self.whip_cream:
            details += ", Whipped Cream"
        return details

    class Meta:
        ordering = ['drink_type__name']
        verbose_name = "Drink Order"
        verbose_name_plural = "Drink Orders"

# Pastry
class PastryType(models.Model):
    name = models.CharField("Pastry Type", max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Pastry(models.Model):
    pastry_type = models.ForeignKey(PastryType, on_delete=models.CASCADE)
    is_warm = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pastry_type.name}, Warmed: {self.is_warm}"

    class Meta:
        ordering = ['pastry_type__name']
        verbose_name = "Pastry Order"
        verbose_name_plural = "Pastry Orders"

# Merch
MERCH_SIZE_CHOICES = [
    (0, 'None'),
    (1, 'S'),
    (2, 'M'),
    (3, 'L'),
    (4, 'XL')
]

class Merch(models.Model):
    name = models.CharField("Merch", max_length=100)
    size = models.PositiveIntegerField(choices=MERCH_SIZE_CHOICES, default=1)
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    # Fields for generic relation:
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order #{self.order.id} - {self.item} x {self.quantity}"