from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
]
