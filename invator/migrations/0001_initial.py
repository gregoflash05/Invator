<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-08-01 03:49
=======
# Generated by Django 3.0.8 on 2020-08-01 00:42
>>>>>>> f02326e024cd785f05d6f37320666dc15a2e1f52

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
                ('item', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.CharField(blank=True, max_length=30, null=True)),
                ('total', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('to_address', models.CharField(blank=True, max_length=500, null=True)),
                ('to_email', models.EmailField(blank=True, max_length=20, null=True)),
                ('to_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('from_full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('from_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('role', models.CharField(blank=True, max_length=150, null=True)),
                ('account_name', models.CharField(blank=True, max_length=150, null=True)),
                ('account_number', models.CharField(blank=True, max_length=150, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=150, null=True)),
                ('from_web_address', models.CharField(blank=True, max_length=150, null=True)),
                ('tax', models.CharField(blank=True, max_length=15, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=150, null=True)),
                ('terms', models.CharField(blank=True, max_length=300, null=True)),
                ('from_email', models.EmailField(blank=True, max_length=20, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('transactions', models.ManyToManyField(to='invator.Transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
