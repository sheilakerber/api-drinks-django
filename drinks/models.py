from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'Name: {self.name} - Description: {self.description}'


class Coffee(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'Name: {self.name} - Type: {self.type} - Country: {self.country}'
