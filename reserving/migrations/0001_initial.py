# Generated by Django 4.0.4 on 2022-06-16 09:50

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
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=1000)),
                ('Second_name', models.CharField(max_length=1000)),
                ('Last_name', models.CharField(max_length=1000)),
                ('Room_number', models.IntegerField()),
                ('Amount_paid', models.IntegerField()),
                ('Email', models.EmailField(max_length=1000)),
                ('Occupation', models.CharField(max_length=1000)),
                ('Nights_of_stay', models.IntegerField()),
                ('Starting_date', models.DateField()),
                ('Ending_date', models.DateField()),
                ('Client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
