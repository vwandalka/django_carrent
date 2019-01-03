# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
    mark = models.CharField(max_length=50, verbose_name='Marka')
    model = models.CharField(max_length=50, verbose_name='Model')
    year = models.IntegerField(verbose_name="Rok produkcji")
    color = models.CharField(max_length=20, null=True, verbose_name="Kolor")
    mileage = models.IntegerField(verbose_name='Przebieg', null=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Samochód'
        verbose_name_plural = 'Samochody'

    def __str__(self):
        return self.mark + ' ' + self.model


class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='username')
    user_name = models.CharField(max_length=20, verbose_name='imię')
    user_surname = models.CharField(max_length=50, verbose_name='nazwisko')
    user_email = models.CharField(max_length=60, verbose_name='email')
    user_phone = models.IntegerField(max_length=15, verbose_name='telefon')
    user_dateofbirth = models.IntegerField(max_length=15, verbose_name='data urodzenia')


class District(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=1)
    desc = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Województwo'
        verbose_name_plural = 'Województwa'

    def __str__(self):
        return self.name + ' (%s)' % self.code

class City(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey('CityType', on_delete='PROTECT')
    dist = models.ForeignKey('District', on_delete='PROTECT')
    desc = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Miasto'
        verbose_name_plural = 'Miasta'

    def __str__(self):
        return self.name


class CityType(models.Model):
    ''' Wieś(5000), Miasteczko(20000), Miasto(200000), Metropoila(powyżej) '''
    name = models.CharField(max_length=50, verbose_name="Rodzaj")
    population = models.IntegerField(verbose_name="Ilość mieszkańców")
    desc = models.TextField(verbose_name="Opis")
    add_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Typ miasta'
        verbose_name_plural = 'Typy miast'

    def __str__(self):
        return self.name