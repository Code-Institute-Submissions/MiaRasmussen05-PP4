from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from random import sample

from .models import Shop, ShopCategory, Blog, Projects, GalleryCategory, Images
from .forms import ReviewForm, CommentForm, ShopForm


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


class AddShopItemView(CreateView, LoginRequiredMixin):
    model = Shop
    template_name = 'shop.html'
    fields = ['title', 'shop_category', 'item', 'image', 'quantity', 'description', 'price', 'status']
    success_url = reverse_lazy('shop')

    def form_valid(self, form):
        if not self.request.user.is_staff:
            raise Http404
        shop = form.save(commit=False)
        shop.save()
        form.save_m2m()
        messages.success(self.request, f"Product '{shop.title}' added successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ShopCategory.objects.all()
        return context


class EditShopItem(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'edit_shopitem.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Shop, pk=pk)

    def get_success_url(self):
        messages.success(self.request, f"Product '{ self.object.title }' updated successfully.")
        return reverse_lazy('shop')


class DeleteShopItem(DeleteView):
    model = Shop
    template_name = 'delete.html'
    success_url = reverse_lazy('shop')

    def get_success_url(self):
        messages.success(self.request, f"Product '{ self.object.title }' deleted successfully.")
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_title'] = (
            "Delete Shop Product"
        )
        context['confirm_message'] = (
            f"Are you sure you want to delete this product '{ self.object.title }'?"
        )
        context['cancel_url'] = reverse_lazy('shop')
        return context


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

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
            comment_form = CommentForm()

            return redirect('blog_post', slug=post.slug)

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


class BlogLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Blog, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_post', args=[slug]))


class ProjectList(ListView):
    model = Projects
    queryset = Projects.objects.filter(status=1).order_by('-created_on')
    template_name = 'portfolio.html'
    paginate_by = 12


class GalleryView(ListView):
    model = Images
    queryset = Images.objects.all()
    template_name = 'gallery.html'
    context_object_name = 'images'
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_images = self.get_queryset()
        categories = GalleryCategory.objects.all()
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = get_object_or_404(GalleryCategory, id=category_id)
            images = Images.objects.filter(category=category)
        else:
            category = None
            images = all_images

        paginator = Paginator(images, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['category'] = category
        context['images'] = page_obj
        context['all_images'] = all_images
        context['categories'] = categories

        return context


def contact(request):
    return render(request, 'contact.html')
