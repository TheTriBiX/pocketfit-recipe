# Generated by Django 5.0.4 on 2024-07-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeservice', '0009_alter_ingredients_id_alter_ingredients_translations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allergy',
            name='foods',
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='translations',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='allergy',
            name='foods',
            field=models.ManyToManyField(blank=True, null=True, to='recipeservice.ingredients'),
        ),
    ]
