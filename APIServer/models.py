# APIServer/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name  # 可选：便于后台显示

class AllergenComponent(models.Model):
    uniprot_id = models.CharField(max_length=20)
    component = models.CharField(max_length=100)
    food_class = models.CharField(max_length=50)
    species_key = models.CharField(max_length=100)
    species_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'allergen_components'
