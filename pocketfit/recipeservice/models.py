from django.db import models

class Ingredients(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, max_length=100, unique=True)
    translations = models.JSONField(null=True)
    Squirrels = models.IntegerField()
    Fats = models.IntegerField()
    Carbohydrates = models.IntegerField() 
    PFC = models.IntegerField() # надо брать из рассчета на m(=100г?)
    comment = models.TextField(max_length=2000)
    same_ingridient = models.ForeignKey("self", related_name='related_ingridients', on_delete=models.CASCADE, null=True, blank=True)
    image = models.CharField(max_length=255)
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
    translations = models.JSONField()
    comment = models.TextField()
    foods = models.ForeignKey(Ingredients, on_delete=models.CASCADE)


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

    ingredient_id = models.IntegerField()
    allergy_id = models.IntegerField()

class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    ingridients = models.JSONField()
    translations = models.JSONField()
    same_dish = models.ForeignKey('self', on_delete=models.CASCADE)
    image = models.CharField(max_length=255)

    class Meta:
        db_table = 'dish'

    def str(self):
        return self.name