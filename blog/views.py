from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import Http404
from random import sample

from .models import Shop, ShopCategory, Blog
from .forms import ReviewForm


def home(request):
    return render(request, 'index.html')


class ShopCategoryView(ListView):
    template_name = 'shop.html'
    context_object_name = 'items'
    model = ShopCategory

    def get_queryset(self):
        selected_category = get_object_or_404(ShopCategory, id=self.kwargs['shop_category_id'])
        if selected_category.name == 'Draft':
            queryset = super().get_queryset().filter(status=0)
        else:
            queryset = super().get_queryset().filter(shop_category=selected_category, status=1)
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
        total_items = len(all_items)
        sample_size = min(6, total_items)
        context['all_items'] = all_items
        context['review_form'] = ReviewForm()
        context['random_items'] = sample(list(all_items), sample_size)
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


class AddShopItemView(View):
    model = Shop
    template_name = 'shop.html'

    def get(self, request, *args, **kwargs):
        categories = ShopCategory.objects.all()
        return render(request, self.template_name, {'categories': categories})

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404
        title = request.POST.get('title')
        shop_category_ids = request.POST.getlist('category')
        categories = ShopCategory.objects.filter(id__in=shop_category_ids)
        item = request.POST.get('item')
        image = request.FILES.get('image')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        price = request.POST.get('price')
        status = request.POST.get('status')
        try:
            new_shop = Shop.objects.create(title=title, item=item, image=image, description=description, price=price, status=status)
        except Exception as e:
            messages.warning(request, f"Failed to add product '{title}': {str(e)}")
            return redirect('add_product')
        for category in categories:
            Shop.shop_category.through.objects.create(shop_id=new_shop.id, shop_category_id=category.id)
        messages.success(request, f"Product '{ title }' added successfully.")
        return redirect('shop')


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 12


class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": comment_form,
            },
        )
