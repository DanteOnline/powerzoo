# Generated by Django 4.2.1 on 2023-05-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_alter_animal_category_alter_card_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]