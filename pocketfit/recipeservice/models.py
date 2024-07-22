from django.db import models
import uuid

class Ingredients(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=100, unique=True)
    translations = models.JSONField(null=True, blank=True)
    Squirrels = models.IntegerField(null=True, blank=True)
    Fats = models.IntegerField(null=True, blank=True)
    Carbohydrates = models.IntegerField(null=True, blank=True) 
    PFC = models.IntegerField(null=True, blank=True) # надо брать из рассчета на m(=100г?)
    comment = models.TextField(max_length=2000, null=True, blank=True)
    same_ingridient = models.ForeignKey("self", related_name='related_ingridients', null=True, blank=True, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        db_table = 'Ingredients'
    def __str__(self):
        return self.name



# Create your models here.
class Allergy(models.Model):
    class Meta:
        db_table = 'allergy'

    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    translations = models.JSONField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    foods = models.ForeignKey(Ingredients, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class UserAllergy(models.Model):
    class Meta:
        db_table = 'user_allergy'
        unique_together = ('user_id', 'allergy_id')

    user_id = models.CharField(max_length=100)
    allergy_id = models.IntegerField()


class IngredientsAllergy(models.Model):
    class Meta:
        db_table = 'IngredientsAllergy'
        unique_together = ('ingredient_id', 'allergy_id')

    ingredient_id = models.IntegerField(null=True, blank=True)
    allergy_id = models.IntegerField(null=True, blank=True)

class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    comment = models.TextField(null=True, blank=True)
    ingridients = models.JSONField(null=True, blank=True)
    translations = models.JSONField(null=True, blank=True)
    same_dish = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'dish'

    def str(self):
        return self.name