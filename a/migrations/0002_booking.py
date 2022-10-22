# Generated by Django 4.1 on 2022-10-11 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_email', models.EmailField(max_length=254)),
                ('p_phone', models.CharField(max_length=100)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a.doctors')),
            ],
        ),
    ]