# Generated by Django 3.0.7 on 2021-09-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_orders_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_t',
            name='totalCost',
            field=models.IntegerField(default=0, max_length=30),
        ),
    ]
