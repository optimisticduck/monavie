# Generated by Django 3.0.7 on 2021-09-13 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210913_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList_T',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailemail', models.CharField(max_length=30)),
            ],
        ),
    ]