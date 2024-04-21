# Generated by Django 5.0.3 on 2024-04-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_remove_ingredient_quantity_alter_ingredient_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipepost',
            name='reciple_label',
            field=models.CharField(choices=[('BEGGINERS', 'BEGGINERS'), ('INTERMEDIATE', 'INTERMEDIATE'), ('EXPERT', 'EXPERT')], default='BEGGINERS', max_length=30),
        ),
    ]
