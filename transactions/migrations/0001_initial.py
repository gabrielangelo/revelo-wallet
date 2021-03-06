# Generated by Django 2.1.7 on 2019-02-28 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('type_transaction', models.SmallIntegerField(choices=[(0, 'OUT'), (1, 'IN')])),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transactions.Wallet'),
        ),
    ]
