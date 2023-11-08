# from django.db import models


# class Products(models.Model):

#     itens = [
#         ('1', 'P'),
#         ('2', 'M'),
#         ('3', 'G'),
#         ('4', 'GG'),
#     ]

#     nome = models.CharField(max_length=255)
#     cod = models.IntegerField(unique=True)
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#     description = models.TextField()
#     qtd = models.IntegerField()
#     size = models.CharField(choices=itens, max_length=255)
#     discount = models.IntegerField()
#     created_at = models.DateField()
#     in_stock = models.BooleanField(default=False)

#     def __str__(self):

#         return self.nome

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="product_images/", null=True, blank=True)
    cod = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    qtd = models.IntegerField()
    discount = models.IntegerField()
    created_at = models.DateField()
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
