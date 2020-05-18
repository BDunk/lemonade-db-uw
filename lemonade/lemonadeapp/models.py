from django.db import models

# Create your models here.

class Salesperson(models.Model):
    name = models.CharField(max_length=200)
    commission = models.FloatField()
    title = models.CharField(max_length=200)

class Order(models.Model):
    salesperson = models.ForeignKey(Salesperson, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    votes = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=None, decimal_places=2)
