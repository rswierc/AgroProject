# Generated by Django 4.1.3 on 2022-12-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cows', '0002_alter_cow_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sorting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('birth_date', 'Data urodzenia'), ('sex', 'Płeć')], max_length=20)),
            ],
        ),
    ]
