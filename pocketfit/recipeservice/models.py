from django.db import models


# Create your models here.
class Allergy(models.Model):
    class Meta:
        db_table = 'allergy'

    name = models.CharField(null=False, max_length=100, unique=True)
    translations = models.JSONField(null=True)

    def __str__(self):
        return self.name


class UserAllergy(models.Model):
    class Meta:
        db_table = 'user_allergy'
        unique_together = ('user_id', 'allergy_id')

    user_id = models.CharField(max_length=100)
    allergy_id = models.IntegerField()


class Ingredients(models.Model):
    class Meta:
        db_table = 'Ingredients'

    name = models.CharField(null=False, max_length=100, unique=True)
    translations = models.JSONField(null=True)

    def __str__(self):
        return self.name


class IngredientsAllergy(models.Model):
    class Meta:
        db_table = 'IngredientsAllergy'
        unique_together = ('ingredient_id', 'allergy_id')

    ingredient_id = models.IntegerField()
    allergy_id = models.IntegerField()
