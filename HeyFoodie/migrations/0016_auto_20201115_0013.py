# Generated by Django 3.0.4 on 2020-11-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeyFoodie', '0015_auto_20201114_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('WAITING', 'Waiting'), ('COOKING', 'Cooking'), ('READYTOPICKUP', 'Ready To Pickup'), ('DONE', 'Done'), ('CANCEL', 'Cancel')], default='WAITING', max_length=20),
        ),
    ]
