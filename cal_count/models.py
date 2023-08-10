from django.db import models

# Create your models here.



class Breakfast(models.Model):
    item_name = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name



class Lunch(models.Model):
    item_name = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name


class Dinner(models.Model):
    item_name = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name
