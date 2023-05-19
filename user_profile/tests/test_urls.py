from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth import get_user_model
from user_profile.views import (
    ProfileDetailView, EditProfileView, BookmarkView, BookmarkListView,
    CartView, AddToCartView, EditCart, OrderListView, OrderDetailView)
from user_profile.models import (
    Profile, Order, OrderItem)


class TestUrls(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_ProfileDetailView_url(self):
        """Tests Profile URL"""
        url = reverse('profile', kwargs={'username': self.user.username})
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProfileDetailView)

    def test_EditProfileView_url(self):
        """Tests Edit Profile URL"""
        url = reverse('edit_profile')
        self.assertEquals(resolve(url).func.view_class, EditProfileView)

    def test_BookmarkView_url(self):
        """Tests Bookmark URL"""
        url = reverse('bookmark', kwargs={'slug': 'example-slug'})
        self.assertEquals(resolve(url).func.view_class, BookmarkView)

    def test_CartView_url(self):
        """Tests Cart Page URL"""
        url = reverse('view_cart')
        self.assertEquals(resolve(url).func.view_class, CartView)

    def test_AddToCartView_url(self):
        """Tests Add to Cart URL"""
        url = reverse('add_to_cart', kwargs={'shop_id': 1})
        self.assertEquals(resolve(url).func.view_class, AddToCartView)

    def test_EditCart_url(self):
        """Tests Edit Cart URL"""
        url = reverse('edit_cart', kwargs={'item_id': 1})
        self.assertEquals(resolve(url).func.view_class, EditCart)
