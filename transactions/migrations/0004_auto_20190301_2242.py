# Generated by Django 2.1.7 on 2019-03-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20190301_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
