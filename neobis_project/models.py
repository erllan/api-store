from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Curt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def total_sum(self):
        total = 0
        orders = Order.objects.filter(cart=self)
        for price in orders:
            total += price.total_price()
        return total


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Order(models.Model):
    cart = models.ForeignKey(Curt, related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    total = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        name = "заказ-" + str(self.product.title)
        return name

    def total_price(self):
        total = self.product.price * self.total
        return total
