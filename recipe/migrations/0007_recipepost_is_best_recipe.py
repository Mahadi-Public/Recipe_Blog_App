# Generated by Django 5.0.1 on 2024-04-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_recipepost_recipe_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipepost',
            name='is_best_recipe',
            field=models.BooleanField(default=False),
        ),
    ]