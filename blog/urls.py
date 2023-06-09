from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/<int:shop_category_id>/', views.ShopCategoryView.as_view(), name='shop_category'),
    path('shop_item/<int:shop_id>/', views.ShopItemView.as_view(), name='shop_item'),
    path('add_shop/', views.AddShopItemView.as_view(), name='add_product'),
    path('shop_item/edit/<int:pk>/', views.EditShopItem.as_view(), name='edit_shop'),
    path('shop_item/delete/<int:pk>/', views.DeleteShopItem.as_view(), name='delete_shop'),
    path('edit-review/<int:pk>/', views.EditReview.as_view(), name='edit-review'),
    path('delete-review/<int:pk>/', views.DeleteReview.as_view(), name='delete-review'),

    path("blog/", views.BlogList.as_view(), name="blog"),
    path("blog_post/", views.BlogList.as_view(), name="blog_list"),
    path('blog_post/<slug:slug>/', views.BlogDetail.as_view(), name='blog_post'),
    path('like/<slug:slug>', views.BlogLike.as_view(), name='blog_like'),
    path('add_blog/', views.AddBlogView.as_view(), name='add_blog'),
    path('blog_post/edit/<slug:slug>/', views.EditBlog.as_view(), name='edit_blog'),
    path('blog_post/delete/<slug:slug>/', views.DeleteBlog.as_view(), name='delete_blog'),
    path('edit-comment/<str:comment_id>/', views.EditCommentView.as_view(), name='edit-comment'),
    path('delete-comment/<str:comment_id>/', views.DeleteCommentView.as_view(), name='delete-comment'),

    path('portfolio/', views.ProjectList.as_view(), name='portfolio'),
    path('add_project/', views.AddProjectView.as_view(), name='add_project'),
    path('project_card/edit/<int:pk>/', views.EditProject.as_view(), name='edit_project'),
    path('project_card/delete/<int:pk>/', views.DeleteProject.as_view(), name='delete_project'),

    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('gallery/<int:category_id>/', views.GalleryView.as_view(), name='gallery_category'),
    path('add-image/', views.AddImageView.as_view(), name='add_image'),
    path('gallery_image/edit/<int:pk>/', views.EditGallery.as_view(), name='edit_image'),
    path('gallery_image/delete/<int:pk>/', views.DeleteGallery.as_view(), name='delete_image'),

    path('contact/', views.contact, name='contact'),
]
