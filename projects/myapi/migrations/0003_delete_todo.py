# Generated by Django 3.2.19 on 2023-07-26 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
    ]