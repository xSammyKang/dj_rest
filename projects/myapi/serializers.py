from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from .models import Shop, Item, UserItem, UserWallet, UserDaily
from django.contrib.auth.password_validation import validate_password
from rest_framework.decorators import api_view
from datetime import datetime

class UserDailySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDaily
        fields = ['id', 'user', 'last_fund', 'last_roll']
    def update(self, instance, validated_data):
        if (validated_data.get("last_fund") == "update"):
            instance.last_fund = datetime.strftime(datetime.now(), '%d%m%y')
        else:
            instance.last_roll = datetime.strftime(datetime.now(), '%d%m%y')
        instance.save()
        return instance

class RandomItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id']

class UserWalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserWallet
        fields = ['user','funds','id']

    def update(self, instance, validated_data):
        instance.funds += validated_data.get("funds")
        instance.save()
        return instance

class BuySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id','item_name','available_quantity']

    def update(self, instance, validated_data):
        curr_user = self.context['request'].user
        curr_item = Item.objects.get(item_name=validated_data.get("item_name"))
        try:
            user_item = UserItem.objects.filter(user=curr_user,item_obj=curr_item)
        except UserItem.DoesNotExist:
            pass
            
        instance.available_quantity -= validated_data.get("available_quantity")
        if (user_item.exists()) :
            curr_user_item = user_item.get()
            curr_user_item.user_quantity += validated_data.get("available_quantity")
            curr_user_item.save()
        else:
            new_user_item = UserItem.objects.create(
                user=curr_user,
                item_obj=curr_item,
                user_quantity=validated_data.get("available_quantity"))
            new_user_item.save()
            
        instance.save()
        return instance

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        curr_user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        UserWallet.objects.create(
            user=curr_user,
            funds=100.00
        )
        curr_user.set_password(validated_data['password'])
        curr_user.save()

        return curr_user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    inventory = serializers.SerializerMethodField()
    wallet = serializers.SerializerMethodField()
    daily = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'groups', 'inventory', 'wallet', 'daily']
    def get_inventory(self, user):
        all_items = user.useritem_set.all()
        return UserItemSerializer(instance=all_items, many=True, context={'request': self.context.get("request")}).data
    def get_wallet(self, curr_user):
        wallet = UserWallet.objects.get_or_create(
            user=curr_user,
            defaults={'funds': 100}
            )
        curr_wallet = curr_user.userwallet
        return UserWalletSerializer(instance=[curr_wallet], many=True, context={'request': self.context.get("request")}).data
    def get_daily(self, curr_user):
        value = UserDaily.objects.get_or_create(
            user=curr_user
        )
        curr_daily = curr_user.userdaily
        return UserDailySerializer(instance=[curr_daily], many=True, context={'request': self.context.get("request")}).data

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id','item_name','add_date','description','available_quantity','shop_name','price']

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    shop_items = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['shop_name','est_date','description', 'shop_items']
    def get_shop_items(self, shop):
        all_items = shop.item_set.all()
        return ItemSerializer(instance=all_items, many=True, context={'request': self.context.get("request")}).data

class UserItemSerializer(serializers.HyperlinkedModelSerializer):
    item_name = serializers.SerializerMethodField()
    class Meta:
        model = UserItem
        fields = ['item_name','user','item_obj','user_quantity']
    def get_item_name(self, user_item):
        return user_item.item_obj.__str__()