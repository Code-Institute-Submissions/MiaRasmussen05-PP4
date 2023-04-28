from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.urls import reverse

from .models import Shop, ShopCategory
from .forms import ReviewForm


def home(request):
    return render(request, 'index.html')


class ShopCategoryView(ListView):
    template_name = 'shop.html'
    context_object_name = 'items'
    model = ShopCategory

    def get_queryset(self):
        selected_category = get_object_or_404(ShopCategory, id=self.kwargs['shop_category_id'])
        queryset = super().get_queryset().filter(shop_category=selected_category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ShopCategory.objects.all()
        selected_category = get_object_or_404(ShopCategory, id=self.kwargs['shop_category_id'])
        context.update({'categories': categories, 'selected_category': selected_category})
        return context


class ShopView(ListView):
    template_name = 'shop.html'
    context_object_name = 'shop_items'
    model = Shop

    def get_queryset(self):
        queryset = super().get_queryset().filter(status=1)
        selected_category_id = self.request.GET.get('category')
        if selected_category_id:
            selected_category = get_object_or_404(ShopCategory, id=selected_category_id)
            queryset = queryset.filter(shop_category=selected_category)
            self.selected_category = selected_category
        else:
            self.selected_category = None
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ShopCategory.objects.all()
        context.update({'categories': categories, 'selected_category': self.selected_category})
        return context


class ShopItemView(DetailView):
    template_name = 'shop_item.html'
    context_object_name = 'shop_item'
    model = Shop

    def get_object(self, queryset=None):
        shop_id = self.kwargs.get('shop_id')
        return get_object_or_404(Shop, id=shop_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_items = Shop.objects.filter(status=1).exclude(id=self.kwargs['shop_id'])
        context['all_items'] = all_items
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        shop_item = self.get_object()
        if form.is_valid():
            review = form.save(commit=False)
            review.comment = shop_item
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has successfully been submitted.')
            return redirect('shop_item', shop_id=shop_item.id)
        else:
            context = self.get_context_data(**kwargs)
            context['review_form'] = form
            return self.render_to_response(context)
