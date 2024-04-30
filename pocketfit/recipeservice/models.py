from django.db import models


# Create your models here.
class Allergy(models.Model):
    class Meta:
        db_table = 'allergy'

    name = models.CharField(null=False, max_length=100, unique=True)
    translations = models.JSONField(null=True)


class UserAllergy(models.Model):
    class Meta:
        db_table = 'user_allergy'

    user_uuidv4 = models.CharField(max_length=100)
    allergy_id = models.IntegerField()
