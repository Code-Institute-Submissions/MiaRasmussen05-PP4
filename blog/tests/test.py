from django.test import TestCase
from django.urls import resolve, reverse
from blog.views import (
    home, ShopView, ShopCategoryView, ShopItemView, AddShopItemView,
    EditShopItem, DeleteShopItem, EditReview, DeleteReview, BlogList,
    BlogDetail, BlogLike, AddBlogView, EditBlog, DeleteBlog, EditCommentView,
    DeleteCommentView, ProjectList, AddProjectView, EditProject, DeleteProject,
    GalleryView, AddImageView, EditGallery, DeleteGallery, contact
)
from blog.models import (ShopCategory, Shop, Review)


class TestUrls(TestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_ShopView_url(self):
        url = reverse('shop')
        self.assertEquals(resolve(url).func.view_class, ShopView)

    def test_ShopCategoryView_url(self):
        url = reverse('shop_category', kwargs={'shop_category_id': 1})
        self.assertEquals(resolve(url).func.view_class, ShopCategoryView)

    def test_ShopItemView_url(self):
        url = reverse('shop_item', kwargs={'shop_id': 1})
        self.assertEquals(resolve(url).func.view_class, ShopItemView)

    def test_AddShopItemView_url(self):
        url = reverse('add_product')
        self.assertEquals(resolve(url).func.view_class, AddShopItemView)

    def test_EditShopItem_url(self):
        url = reverse('edit_shop', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditShopItem)

    def test_DeleteShopItem_url(self):
        url = reverse('delete_shop', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteShopItem)

    def test_EditReview_url(self):
        url = reverse('edit-review', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditReview)

    def test_DeleteReview_url(self):
        url = reverse('delete-review', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteReview)
