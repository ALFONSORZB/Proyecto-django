# Generated by Django 4.2 on 2024-10-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crude', '0011_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Imagen'),
        ),
    ]
