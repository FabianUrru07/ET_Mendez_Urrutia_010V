# Generated by Django 4.0.5 on 2022-06-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='static/img/', verbose_name='Imagen'),
        ),
    ]