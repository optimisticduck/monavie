# Generated by Django 3.0.7 on 2021-09-12 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_orders_t_totalcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_t',
            name='itemsOrdered',
            field=models.CharField(default=0, max_length=40),
        ),
    ]