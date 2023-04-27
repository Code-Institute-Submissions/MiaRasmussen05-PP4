from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from .models import Shop, ShopCategory


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
