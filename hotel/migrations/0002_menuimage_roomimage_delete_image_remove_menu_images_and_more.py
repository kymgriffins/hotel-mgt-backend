# Generated by Django 4.1.5 on 2023-04-11 15:34

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='MenuImages')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='RoomImage')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='images',
        ),
        migrations.RemoveField(
            model_name='room',
            name='images',
        ),
        migrations.AddField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room'),
        ),
        migrations.AddField(
            model_name='menuimage',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='MenuImage', to='hotel.menuimage'),
        ),
        migrations.AddField(
            model_name='room',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='RoomImage', to='hotel.roomimage'),
        ),
    ]
