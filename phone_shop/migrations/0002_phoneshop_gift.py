# Generated by Django 5.0.2 on 2024-02-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneshop',
            name='gift',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Укажите подарок к покупке'),
        ),
    ]
