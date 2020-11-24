# Generated by Django 3.0.4 on 2020-11-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeyFoodie', '0011_auto_20201113_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_rating',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='user_rating',
            name='menu',
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('complete', 'Complete'), ('waiting', 'Waiting')], default='waiting', max_length=20),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='User_Rating',
        ),
    ]
