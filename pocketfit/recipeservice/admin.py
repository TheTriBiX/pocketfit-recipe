from django.contrib import admin
from recipeservice import models
# Register your models here.
admin.site.register(models.Allergy)
admin.site.register(models.UserAllergy)
admin.site.register(models.Ingredients)
admin.site.register(models.IngredientsAllergy)
admin.site.register(models.Dish)
