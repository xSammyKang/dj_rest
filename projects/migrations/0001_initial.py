# Generated by Django 3.2.19 on 2023-09-12 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(verbose_name='date added')),
                ('description', models.CharField(max_length=2000)),
                ('available_quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('est_date', models.DateTimeField(verbose_name='date established')),
                ('description', models.CharField(default='Description here', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funds', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_quantity', models.IntegerField(default=0)),
                ('item_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_fund', models.CharField(default='270395', max_length=10)),
                ('last_roll', models.CharField(default='270395', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='shop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.shop'),
        ),
    ]
