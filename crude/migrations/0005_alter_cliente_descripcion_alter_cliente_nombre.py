# Generated by Django 4.2 on 2024-10-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crude', '0004_cliente_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.TextField(blank=True, null=True),
        ),
    ]
