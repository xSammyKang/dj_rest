"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from .myapi.views import UserViewSet, GroupViewSet, ItemViewSet, ShopViewSet, UserItemViewSet, RegisterViewSet, BuyViewSet, UserWalletViewSet, RandomItemViewSet, UserDailyViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'groups', GroupViewSet)
router.register(r'items', ItemViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'useritems', UserItemViewSet)
router.register(r'buy', BuyViewSet, basename='buy')
router.register(r'addfunds', UserWalletViewSet)
router.register(r'randomitem', RandomItemViewSet, basename='randomitem')
router.register(r'userdaily', UserDailyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^auth/', include('djoser.urls')),
]