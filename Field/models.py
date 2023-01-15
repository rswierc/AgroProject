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
    area = models.FloatField()
    location = models.CharField(max_length=15, choices=LOCATION_CHOISES)
    field_image = models.ImageField(blank = True, null=True, upload_to="images/")
    soil_richness = models.FloatField(blank = True, null = True)
    acidity = models.FloatField(blank = True, null=True)
    last_seed = models.CharField(max_length=10, null=True, blank = True)
    present_seed = models.CharField(max_length=10, blank = True, null=True)

class Spraying(models.Model):
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(blank = True, null=True)


class Fertilization(models.Model):
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(blank = True, null=True)

class Harvest(models.Model):
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    harvest_date = models.DateField(blank = True, null=True)
    hight = models.FloatField(blank = True, null=True)


class NPK_Field(models.Model):
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    measurement_date = models.DateField(blank = True, null = True)
    nitrogen_field = models.FloatField(blank=True, null=True)
    phosphorus_field = models.FloatField(blank=True, null=True)
    potassium_field = models.FloatField(blank=True, null=True)


class NPK_Product(models.Model):
    nitrogen_product = models.FloatField(blank=True, null=True)
    phosphorus_product = models.FloatField(blank=True, null=True)
    potassium_product = models.FloatField(blank=True, null=True)



