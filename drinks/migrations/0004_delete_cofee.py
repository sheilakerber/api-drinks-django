# Generated by Django 4.1.3 on 2022-11-17 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0003_rename_cofees_cofee'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cofee',
        ),
    ]
