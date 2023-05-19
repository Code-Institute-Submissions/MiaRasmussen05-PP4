from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth import get_user_model
from user_profile.views import (
    ProfileDetailView, BookmarkView, BookmarkListView, CartView, OrderListView,
    OrderDetailView)
from user_profile.models import (
    Profile, Order, OrderItem)


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_ProfileDetailView_url(self):
        """Tests Profile URL"""
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_CreateProfileView_url(self):
        """Tests Create Profile URL"""
        url = reverse('create_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_EditProfileView_url(self):
        """Tests Edit Profile URL"""
        url = reverse('edit_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.view_class, EditProfileView)

    def test_BookmarkListView_url(self):
        """Tests Bookmark Page URL"""
        url = reverse('bookmark_list', kwargs={'username': self.user.username})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.view_class, BookmarkListView)

    def test_BookmarkView_url(self):
        """Tests Bookmark URL"""
        url = reverse('bookmark', kwargs={'slug': 'example-slug'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.view_class, BookmarkView)

    def test_CartView_url(self):
        """Tests Cart Page URL"""
        url = reverse('view_cart')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(
        response.resolver_match.func.view_class, CartView)

    def test_AddToCartView_url(self):
        """Tests Add to Cart URL"""
        url = reverse('add_to_cart', kwargs={'shop_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.view_class, AddToCartView)

    def test_EditCart_url(self):
        """Tests Edit Cart URL"""
        url = reverse('edit_cart', kwargs={'item_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.view_class, EditCart)

    def test_delete_from_cart_url(self):
        """Tests Delete from Cart URL"""
        url = reverse('delete_from_cart', kwargs={'item_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func, delete_from_cart)

    def test_OrderListView_url(self):
        """Tests Orders URL"""
        url = reverse('orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.view_class, OrderListView)

    def test_CreateOrderView_url(self):
        """Tests Create Order URL"""
        url = reverse('create_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.view_class, CreateOrderView)
