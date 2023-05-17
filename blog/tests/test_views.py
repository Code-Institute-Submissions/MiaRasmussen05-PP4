from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import (
    ShopCategory, Shop, Review, Blog, Comment, Projects, Images)


class TestViews(TestCase):
    """Tests Views"""
    def setUp(self):
        """
        Sets up the user and models for the tests
        """

        User = get_user_model()
        self.client = Client()
        self.user = User.objects.create_user(
            username='jane', email='test@test.com', password='janepassword'
        )

        self.shop_category = ShopCategory.objects.create(name='Category 1')

        self.shop1 = Shop.objects.create(
            title='Item 1', shop_category=self.shop_category,
            price=2.50, status=1)
        self.shop2 = Shop.objects.create(
            title='Item 2', shop_category=self.shop_category,
            price=3.00, status=1)
        self.shop3 = Shop.objects.create(
            title='Item 3', shop_category=self.shop_category,
            price=2.00, status=0)

    def test_home_view(self):
        """
        Test the home view for the index page
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_shop_category_view(self):
        """
        Test the ShopCategoryView to see shop categories
        """
        response = self.client.get(reverse('shop'))
        self.client.login(username='jane', password='janepassword')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')
        self.assertContains(response, self.shop_category.name)

    def test_shop_view(self):
        """
        Test the ShopView for the shop page
        """
        url = reverse('shop')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')

        self.assertIn(self.shop1, response.context['shop_items'])
        self.assertIn(self.shop2, response.context['shop_items'])
        self.assertNotIn(self.shop3, response.context['shop_items'])

        self.assertIn(self.shop_category, response.context['categories'])

        self.assertIsNone(response.context['selected_category'])
