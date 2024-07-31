import uuid
import re
from django.core.exceptions import ValidationError
from django.db import models

class Ingredients(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=100, unique=True)
    translations = models.JSONField(null=True)
    Squirrels = models.IntegerField(null=True, blank=True)
    Fats = models.IntegerField(null=True, blank=True)
    Carbohydrates = models.IntegerField(null=True, blank=True) 
    PFC = models.IntegerField(null=True, blank=True) # надо брать из рассчета на m(=100г?)
    comment = models.TextField(max_length=2000, null=True, blank=True)
    same_ingridient = models.ForeignKey("self", related_name='related_ingridients', null=True, blank=True, on_delete=models.CASCADE) # Убрать это поле не нужно
    image = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        db_table = 'Ingredients'
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        self.translations = {"ru" : self.name} # Здесь необходимо вместо ru вытягивать язык пользователя по умолчанию???   
        super(Ingredients, self).save(*args, **kwargs)
    def clean(self):
        super().clean()
        url_pattern = re.compile(
            r'^(http|https)://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-._?&=/]*$' # Исправить реглярку 
        )
        if self.image and not url_pattern.match(self.image):
            raise ValidationError('Invalid URL format for image field.')

class Allergy(models.Model):
    class Meta:
        db_table = 'allergy'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    translations = models.JSONField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    foods = models.ManyToManyField(Ingredients, blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        self.translations = {"ru": self.name}  # Здесь необходимо вместо ru вытягивать язык пользователя по умолчанию???
        super(Allergy, self).save(*args, **kwargs)


class UserAllergy(models.Model):
    class Meta:
        db_table = 'user_allergy'
        unique_together = ('user_id', 'allergy_id')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    allergy_id = models.IntegerField()

class IngredientsCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredients, related_name='categories')
    translations = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'ingredients_category'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        self.translations = {"ru": self.name}
        super().save(*args, **kwargs)


class IngredientsAllergy(models.Model):
    class Meta:
        db_table = 'IngredientsAllergy'
        unique_together = ('ingredient_id', 'allergy_id')

    ingredient_id = models.IntegerField(null=True, blank=True)
    allergy_id = models.IntegerField(null=True, blank=True)

class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    comment = models.TextField(null=True, blank=True)
    components = models.JSONField(null=True, blank=True)  # Это поле необходимо для того что бы передавать кол-во ин-ов
    translations = models.JSONField(null=True, blank=True)
    white_list = models.ForeignKey("IngredientsCategory", null=True, blank=True, on_delete=models.CASCADE, related_name='white_list_dishes')
    ingredients = models.ForeignKey("IngredientsCategory", null=True, blank=True, on_delete=models.CASCADE, related_name='ingredient_dishes')
    image = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'dish'

    def clean(self):
        super().clean()
        url_pattern = re.compile(
            r'^(http|https)://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-._?&=/]*$' # Исправить реглярку 
        )
        if self.image and not url_pattern.match(self.image):
            raise ValidationError('Invalid URL format for image field.')
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        self.translations = {"ru": self.name}
        super(Dish, self).save(*args, **kwargs)

    def str(self):
        return self.name