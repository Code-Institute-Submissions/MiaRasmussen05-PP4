from django.urls import path, include
from . import views

urlpatterns = [
    path('<username>/', views.ProfileDetailView.as_view(), name='profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),

    path('bookmarks/<str:username>/', views.BookmarkListView.as_view(), name='bookmark_list'),
    path('bookmark/<slug:slug>/bookmark/', views.BookmarkView.as_view(), name='bookmark'),
]
