# Generated by Django 3.0.4 on 2020-03-31 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapangan', '0003_auto_20200331_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lapangan',
            name='gambar',
            field=models.ImageField(blank=True, default='images/lapangan/no_img.jpeg', upload_to='images/lapangan/'),
        ),
    ]
