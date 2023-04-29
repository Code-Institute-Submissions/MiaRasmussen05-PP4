from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect

from blog.models import Blog
from .models import Profile
from .forms import ProfileForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class CreateProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        if not hasattr(self.request.user, 'profile'):
            profile = form.save(commit=False)
            profile.user = self.request.user
            profile.save()
        return redirect(self.success_url)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_profile.html'

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        profile = form.save(commit=False)
        user = self.request.user
        profile.user = user
        profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


class BookmarkView(View, LoginRequiredMixin):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)
        if post.bookmarked.filter(id=request.user.id).exists():
            post.bookmarked.remove(request.user)
        else:
            post.bookmarked.add(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class BookmarkListView(ListView, LoginRequiredMixin):
    model = Blog
    context_object_name = 'bookmark'
    template_name = 'bookmarks.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        queryset = self.model.objects.filter(bookmarked=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username')
        return context
