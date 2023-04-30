from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.views.generic import DetailView, CreateView, UpdateView, ListView, TemplateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.http import Http404
from decimal import Decimal

from blog.models import Shop, Blog
from .models import Profile, Order, OrderItem
from .forms import ProfileForm, CreateOrderForm


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


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, shop_id):
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))
        shop_item = get_object_or_404(Shop, id=shop_id)
        current_quantity = cart.get(str(shop_id), 0)
        new_quantity = current_quantity + quantity

        if new_quantity > 5:
            messages.warning(request, f"You can only add up to 5 {shop_item.title} {shop_item.item}'s to your cart! 5 {shop_item.title} {shop_item.item}'s now in your cart.")
            cart[str(shop_id)] = 5
        else:
            cart[str(shop_id)] = new_quantity
            if quantity > 1:
                messages.success(request, f"{quantity} {shop_item.title} {shop_item.item}'s has been added to your cart.")
            else:
                messages.success(request, f"{quantity} {shop_item.title} {shop_item.item} has been added to your cart.")

        request.session['cart'] = cart

        previous_url = request.META.get('HTTP_REFERER')
        if previous_url and '/shop/' in previous_url:
            redirect_url = reverse('shop')
        else:
            redirect_url = reverse('shop_item', kwargs={'shop_id': shop_id})

        return HttpResponseRedirect(redirect_url)


class EditCart(LoginRequiredMixin, UpdateView):
    def post(self, request, item_id):
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))
        shop_item = get_object_or_404(Shop, id=item_id)

        if quantity <= 0:
            del cart[str(item_id)]
            messages.success(request, f"{shop_item.title} has been removed from your cart.")
        elif quantity > 5:
            messages.warning(request, f"You can only add up to 5 {shop_item.title} to your cart!")
            cart[str(item_id)] = 5
        else:
            cart[str(item_id)] = quantity
            messages.success(request, f"{shop_item.title} quantity has been updated to {quantity} in your cart!")

        request.session['cart'] = cart
        return redirect('view_cart')


def delete_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    shop_item = get_object_or_404(Shop, id=item_id)
    if str(item_id) in cart:
        del cart[str(item_id)]
    messages.success(request, f"{shop_item.title} {shop_item.item} has been deleted from your cart.")
    request.session['cart'] = cart
    return redirect('view_cart')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'order.html'
    success_url = reverse_lazy('cart')

    def form_valid(self, form):
        form.instance.user = self.request.user
        cart_items = self.request.POST.getlist('cart_items[]')
        order_items = []
        for item in cart_items:
            item_id, quantity = item.split(':')
            shop_item = get_object_or_404(Shop, id=item_id)
            order_item = OrderItem(
                order=form.instance,
                item=shop_item,
                quantity=quantity,
                price=shop_item.price
            )
            order_items.append(order_item)
        OrderItem.objects.bulk_create(order_items)

        del self.request.session['cart']

        messages.success(self.request, 'Your order was placed successfully!')

        return super().form_valid(form)

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
