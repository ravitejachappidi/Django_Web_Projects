from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    hear_about = models.CharField(max_length=100)
    visit_store = models.BooleanField()

    def __str__(self):
        return self.name
