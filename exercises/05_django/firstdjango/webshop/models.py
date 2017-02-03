from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    quantity = models.IntegerField(default=0)

    def sell(self):
        # decrease the quantity of the product by one.
        self.quantity-=1
        self.save()
        return self.quantity
# from webshop.models import Product
# p = Product(title="Teddy Bear", description="Huge fluffy teddy-bear", quantity=10)
# print(p.title)
# p.sell()