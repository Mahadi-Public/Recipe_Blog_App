# Generated by Django 5.0.3 on 2024-04-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_remove_recipepost_reciple_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepost',
            name='recipe_label',
            field=models.CharField(choices=[('BEGGINERS', 'BEGGINERS'), ('INTERMEDIATE', 'INTERMEDIATE'), ('EXPERT', 'EXPERT')], default='BEGGINERS', max_length=30),
        ),
    ]