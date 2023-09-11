from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime

# Create your models here.
MAX_SIZE = 10


class UserDaily(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_fund = models.CharField(max_length = 10, default=("270395"))
    last_roll = models.CharField(max_length = 10, default=("270395"))
    def __str__(self):
        return self.user.username

class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    funds = models.FloatField(default=0)
    def __str__(self):
        return self.user.username

class Shop(models.Model):
    shop_name = models.CharField(max_length = 200, primary_key=True)
    est_date = models.DateTimeField("date established")
    description = models.CharField(max_length = 2000, default="Description here")
    def __str__(self):
        return self.shop_name
    def established_recently(self):
        return self.est_date >= timezone.now() - datetime.timedelta(days=1)

class Item(models.Model):
    item_name = models.CharField(max_length = 200)
    add_date = models.DateTimeField("date added")
    description = models.CharField(max_length = 2000)
    available_quantity = models.IntegerField(default=0)
    shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.item_name
    def new_item(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days=1)

class UserItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_obj = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.item_obj.item_name