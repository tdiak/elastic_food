# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Ingredient(models.Model):
    UNITS = (
        ('szt', "Sztuka"),
        ('g', "Gram"),
        ('ml', "Mililitr")
    )
    name = models.CharField(
        verbose_name="Nazwa",
        max_length=120,
        unique=True
    )
    quantity = models.FloatField(
        verbose_name="Ilość"
    )
    unit = models.CharField(
        verbose_name="Jednostka",
        choices=UNITS,
        max_length=30
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Składnik"
        verbose_name_plural = "Składniki"


@python_2_unicode_compatible
class Recipe(models.Model):
    LEVELS = (
        ('easy', "Łatwy"),
        ('medium', "Średni"),
        ('hard', "Trudny")
    )
    name = models.CharField(
        verbose_name="Nazwa",
        max_length=120,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name="Składniki"
    )
    level = models.CharField(
        verbose_name="Poziom trudności",
        choices=LEVELS,
        max_length=10
    )
    image = models.ImageField(
        verbose_name="Zdjęcie",
        upload_to='recipes',
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Przepis"
        verbose_name_plural = "Przepisy"


@python_2_unicode_compatible
class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name="Przepis"
    )
    description = models.TextField(
        verbose_name="Opis"
    )
    order = models.PositiveSmallIntegerField(
        verbose_name="Kolejność"
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Krok"
        verbose_name_plural = "Kroki"
