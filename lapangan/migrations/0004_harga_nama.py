# Generated by Django 3.0.5 on 2020-04-05 10:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lapangan', '0003_jadwal'),
    ]

    operations = [
        migrations.AddField(
            model_name='harga',
            name='nama',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]