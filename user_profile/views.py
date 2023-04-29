from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, ListView, TemplateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect

from blog.models import Blog
from .models import Profile
from blog.models import Shop
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


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = []
        total_quantity = 0
        total = 0
        shipping_fee = 2
        free_shipping = 55
        total_with_shipping = 0

        for item_id, quantity in self.request.session.get('cart', {}).items():
            shop_item = get_object_or_404(Shop, id=item_id)
            cart_items.append({'id': item_id, 'title': shop_item.title, 'price': shop_item.price, 'quantity': quantity, 'total': shop_item.price * quantity, 'image': shop_item.image})
            total += shop_item.price * quantity
            total_with_shipping += shop_item.price * quantity
            total_quantity += quantity

        if len(cart_items) == 0:
            total_with_shipping = 0
        else:
            if total >= free_shipping:
                shipping_fee = 0
            total_with_shipping += Decimal(str(shipping_fee))

        context['cart_items'] = cart_items
        context['total_quantity'] = total_quantity
        context['total'] = total
        context['shipping_fee'] = shipping_fee
        context['total_with_shipping'] = total_with_shipping
        context['free_shipping'] = free_shipping
        return context
