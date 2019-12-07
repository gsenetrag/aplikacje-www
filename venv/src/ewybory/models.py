from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Wyborcy(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    PESEL = models.CharField(max_length=45)
    nr_dowodu = models.CharField(max_length=45)
    wojewodztwo = models.CharField(max_length=45)


# class Wojewodztwo(models.Model):
#     nazwa = models.CharField(max_length=45)
#     def __init__(self, nazwa):
#         self.nazwa = nazwa


# class Partie(models.Model):
#     nazwa = models.CharField(max_length=45)
#     ilosc_glosow = models.IntegerField()


class Kandydaci(models.Model):
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    liczba_glosow = models.IntegerField()
    wojewodztwo = models.CharField(max_length=45)
    partia = models.CharField(max_length=45)
    nr_partii = models.IntegerField()

