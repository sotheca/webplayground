# Generated by Django 2.2.5 on 2019-09-10 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajero', '0004_auto_20190910_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hilo',
            options={'ordering': ['-fecha_actualizar']},
        ),
        migrations.RenameField(
            model_name='hilo',
            old_name='update',
            new_name='fecha_actualizar',
        ),
    ]