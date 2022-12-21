from django.db import models

# Create your models here.
class Cow(models.Model):
    MALE = 'Byk'
    FEMALE = 'Krowa'
    SEX_CHOICES = [
        (MALE, 'Byk'),
        (FEMALE, 'Krowa'),
    ]

    earring_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=5, choices=SEX_CHOICES)

    buyer = models.CharField(max_length=20, blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    sale_date = models.DateField(blank=True, null=True)
    calving_date = models.DateField(blank=True, null=True) #wycielenie
    estrus_date = models.DateField(blank=True, null=True) #ruja
    # notatki
