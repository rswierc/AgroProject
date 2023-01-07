from django.db import models

# Create your models here.
class Field(models.Model):
    LOCATION_CHOISES = [
        ("Kobylno", "Kobylno"),
        ("Bierdzany", "Bierdzany"),
        ("Kopalina", "Kopalina"),
        ("Inna", "Inna"),
    ]
    field_number = models.CharField(max_length=10, unique=True)
    ar_label = models.CharField(max_length=10, unique=True)
    mr_label = models.CharField(max_length=10, unique=True)
    area = models.FloatField()
    location = models.CharField
    field_image = models.ImageField()
