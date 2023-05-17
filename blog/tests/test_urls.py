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

    def test_BlogList_url(self):
        url = reverse('blog')
        self.assertEquals(resolve(url).func.view_class, BlogList)

    def test_BlogList_post_url(self):
        url = reverse('blog_list')
        self.assertEquals(resolve(url).func.view_class, BlogList)

    def test_BlogDetail_url(self):
        url = reverse('blog_post', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, BlogDetail)

    def test_BlogLike_url(self):
        url = reverse('blog_like', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, BlogLike)

    def test_AddBlogView_url(self):
        url = reverse('add_blog')
        self.assertEquals(resolve(url).func.view_class, AddBlogView)

    def test_EditBlog_url(self):
        url = reverse('edit_blog', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, EditBlog)

    def test_DeleteBlog_url(self):
        url = reverse('delete_blog', kwargs={'slug': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteBlog)

    def test_EditCommentView_url(self):
        url = reverse('edit-comment', kwargs={'comment_id': 1})
        self.assertEquals(resolve(url).func.view_class, EditCommentView)

    def test_DeleteCommentView_url(self):
        url = reverse('delete-comment', kwargs={'comment_id': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteCommentView)

    def test_ProjectList_url(self):
        url = reverse('portfolio')
        self.assertEquals(resolve(url).func.view_class, ProjectList)

    def test_AddProjectView_url(self):
        url = reverse('add_project')
        self.assertEquals(resolve(url).func.view_class, AddProjectView)

    def test_EditProject_url(self):
        url = reverse('edit_project', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditProject)

    def test_DeleteProject_url(self):
        url = reverse('delete_project', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteProject)

    def test_GalleryView_url(self):
        url = reverse('gallery')
        self.assertEquals(resolve(url).func.view_class, GalleryView)

    def test_GalleryView_category_url(self):
        url = reverse('gallery_category', kwargs={'category_id': 1})
        self.assertEquals(resolve(url).func.view_class, GalleryView)

    def test_AddImageView_url(self):
        url = reverse('add_image')
        self.assertEquals(resolve(url).func.view_class, AddImageView)

    def test_EditGallery_url(self):
        url = reverse('edit_image', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, EditGallery)

    def test_DeleteGallery_url(self):
        url = reverse('delete_image', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, DeleteGallery)

    def test_contact_url(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)
