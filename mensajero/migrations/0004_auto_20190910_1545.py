# Generated by Django 2.2.5 on 2019-09-10 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajero', '0003_auto_20190910_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hilo',
            options={'ordering': ['-update']},
        ),
        migrations.RenameField(
            model_name='hilo',
            old_name='fecha_actualizar',
            new_name='update',
        ),
    ]
