# Generated by Django 2.2.12 on 2020-10-02 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0002_auto_20201002_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timings', models.CharField(choices=[('breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Lunch', 'Lunch')], max_length=100)),
                ('date_booked', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('item_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MessStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MessUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='MessDetails',
        ),
        migrations.AddField(
            model_name='bookings',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess.MessUsers'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='item_booked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess.Items'),
        ),
    ]