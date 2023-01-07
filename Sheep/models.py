from django.db import models

# Create your models here.
class Sheep(models.Model):
    MALE = 'Owca'
    FEMALE = 'Baran'
    SEX_CHOICES = [
        (MALE, 'Owca'),
        (FEMALE, 'Baran'),
    ]

    earring_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=5, choices=SEX_CHOICES)

    buyer = models.CharField(max_length=20, blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    sale_date = models.DateField(blank=True, null=True, )
    calving_date = models.DateField(blank=True, null=True) #wycielenie
    estrus_date = models.DateField(blank=True, null=True) #ruja
    note = models.TextField(blank=True, max_length=1000, null=True)

