# Generated by Django 4.2.16 on 2024-11-18 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('insurance_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('physician_name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.customer')),
            ],
        ),
    ]