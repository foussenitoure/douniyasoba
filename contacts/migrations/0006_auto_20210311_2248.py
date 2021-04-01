# Generated by Django 3.1.5 on 2021-03-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20210310_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sexe',
            field=models.CharField(choices=[('HOMME', 'Homme'), ('FEMME', 'Femme')], max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('PERSONNE', 'Personne'), ('SOCIETE', 'Societe')], max_length=30),
        ),
    ]