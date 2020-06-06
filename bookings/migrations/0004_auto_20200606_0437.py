# Generated by Django 3.0.6 on 2020-06-06 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20200606_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Lunas', 'Selesai'), ('Belum Lunas', 'Belum Selesai')], max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.BookingTime')),
            ],
        ),
        migrations.AddField(
            model_name='bookingtime',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Booking'),
        ),
        migrations.AddField(
            model_name='bookingtime',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Time'),
        ),
    ]
