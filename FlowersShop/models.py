from django.db import models


class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
