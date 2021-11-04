from django.db import models


class Product(models.Model):

    PRODUCT_CATEGORY = (
        ('B', 'Barato'),
        ('M', 'Médio'),
        ('C', 'Caro')
    )

    code = models.CharField(primary_key=True, unique=True, max_length=10)
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    unit = models.CharField(max_length=10)
    product_category = models.CharField(
        max_length=10, choices=PRODUCT_CATEGORY, blank=True, null=True)

    class Meta:
        db_table = 'Product'
