# Generated by Django 2.2.4 on 2019-09-04 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20190904_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='usuario',
        ),
    ]
