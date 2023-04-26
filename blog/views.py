from django.shortcuts import render
from django.views import generic
from .models import Shop


def shop_category(request, shop_category_id):
    categories = ShopCategory.objects.all()
    selected_category = get_object_or_404(ShopCategory, id=shop_category_id)
    items = Shop.objects.filter(shop_category=selected_category)
    context = {'categories': categories, 'items': items, 'selected_category': selected_category}

    return render(request, 'shop.html', context)


def shop(request):
    categories = ShopCategory.objects.all()
    queryset = Shop.objects.filter(status=1)
    selected_category_id = request.GET.get('category')
    if selected_category_id:
        selected_category = get_object_or_404(ShopCategory, id=selected_category_id)
        shop_items = queryset.filter(shop_category=selected_category)
    else:
        selected_category = None
        shop_items = queryset.all()

    return render(request, 'shop.html', {'categories': categories, 'selected_category': selected_category, 'shop_items': shop_items})
