from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# env: ecommerce_env
# activate env
# install django
# create django project with name <ecommerce>
# create app with name <users>, <product>
# create Model -> Product in product app
# makemigrations
# migrate
# create object of Product in shell