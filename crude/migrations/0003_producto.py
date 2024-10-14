# Generated by Django 4.2 on 2024-10-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crude', '0002_alter_cliente_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('stock', models.PositiveIntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
