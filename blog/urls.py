from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/<int:shop_category_id>/', views.ShopCategoryView.as_view(), name='shop_category'),
    path('shop_item/<int:shop_id>/', views.ShopItemView.as_view(), name='shop_item'),
    # path('add_shop/shop/', views.ShopCreateView, name='add_shop'),
    path('add/', views.AddShopItemView.as_view(), name='add_product'),
]
