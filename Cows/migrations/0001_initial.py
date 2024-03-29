# Generated by Django 4.1.3 on 2022-12-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earring_number', models.CharField(max_length=10, unique=True)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[('Byk', 'Byk'), ('Krowa', 'Krowa')], max_length=5)),
                ('buyer', models.CharField(max_length=20)),
                ('sale_price', models.FloatField(blank=True, null=True)),
                ('sale_date', models.DateField(blank=True, null=True)),
                ('calving_date', models.DateField(blank=True, null=True)),
                ('estrus_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
