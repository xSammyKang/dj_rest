from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .models import Shop, Item, UserItem, UserWallet
from .serializers import UserSerializer, GroupSerializer, ItemSerializer, ShopSerializer, UserItemSerializer, RegisterSerializer, BuySerializer, UserWalletSerializer, RandomItemSerializer

class RandomItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = RandomItemSerializer

class UserWalletViewSet(viewsets.ModelViewSet):
    queryset = UserWallet.objects.all()
    serializer_class = UserWalletSerializer

class BuyViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = BuySerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    #@api_view(['PUT'])
    #def put(request):
    #    new_shop = ShopSerializer({
    #        'shop_name': request.current_shop.shop_name,
    #        'est_date': request.current_shop.est_date,
    #        'description': request.current_shop.description
    #    })

    #    if new_shop.is_valid():
    #        new_shop.save()
    #        return Response(new_shop.data)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserItemViewSet(viewsets.ModelViewSet):
    queryset = UserItem.objects.all()
    serializer_class = UserItemSerializer
