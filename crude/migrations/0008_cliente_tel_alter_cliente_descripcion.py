# Generated by Django 4.2 on 2024-10-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crude', '0007_alter_cliente_apellido_alter_cliente_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='descripcion',
            field=models.TextField(max_length=20),
        ),
    ]