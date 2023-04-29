from django.urls import path, include
from . import views

urlpatterns = [
    path('<username>/', views.ProfileDetailView.as_view(), name='profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),

    path('bookmarks/<str:username>/', views.BookmarkListView.as_view(), name='bookmark_list'),
    path('bookmark/<slug:slug>/bookmark/', views.BookmarkView.as_view(), name='bookmark'),

    path('profile/cart/', views.CartView.as_view(), name='view_cart'),
    path('shop/add-to-cart/<int:shop_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('edit_cart/<int:item_id>/', views.EditCart.as_view(), name='edit_cart'),
]
