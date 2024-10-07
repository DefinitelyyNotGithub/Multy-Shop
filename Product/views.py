from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductModel, Category, DiscountPrice, RecentlyViewedProducts
from .forms import UserReviewForm


class NavBarView(TemplateView):
    template_name = 'includes/NavBar.html'

    def get_context_data(self, **kwargs):
        context = super(NavBarView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context



class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = ProductModel
    paginate_by = 33
    context_object_name = 'obj'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['global_off'] = DiscountPrice.objects.filter(apply_to_all_products=True, is_active=True).last()
        active_discounts = DiscountPrice.objects.filter(is_active=True)
        context['active_discounts'] = ProductModel.objects.filter(discount__in=active_discounts)
        return context

    def get_queryset(self, **kwargs):

        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        color = request.GET.getlist('color')
        size = request.GET.getlist('size')
        sorted_by = request.GET.get('sorted_by')

        if self.kwargs:
            queryset = ProductModel.objects.filter(category__slug=self.kwargs.get('cat')).distinct()

        if 'favorites' in request:
            queryset = ProductModel.objects.filter(favorites__phone=request.user.phone)

        else:
            queryset = ProductModel.objects.all()

        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price, price__gte=min_price)

        if color:
            queryset = queryset.filter(color__title__in=color)

        if size:
            queryset = queryset.filter(size__title__in=size)

        if sorted_by:
            if sorted_by == 'latest':
                queryset = queryset.order_by('-add_date')
            elif sorted_by == 'popularity':
                queryset = queryset.order_by('-sell_count')
            elif sorted_by == 'off_price':
                queryset = queryset.filter(discount__is_active=True).order_by('-discount__discount_rate')

            elif sorted_by == 'all':
                queryset = queryset

            # if sorted_by == 'rating':
            #   queryset = queryset.order_by()

        return queryset


class UserFavoriteList(TemplateView):
    template_name = 'product/user_liked_products.html'


def add_to_favorites(request, pk):
    from Account.models import User
    product = get_object_or_404(ProductModel, id=pk)

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if product in user.favorites.all():
            user.favorites.remove(product)
        else:
            user.favorites.add(product)
    else:
        if 'favorites' in request.session:
            if product.id in request.session['favorites']:
                request.session['favorites'].remove(product.id)
            else:
                request.session['favorites'].append(product.id)
        else:
            request.session['favorites'] = []
            request.session['favorites'].append(product.id)

        request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER', '/'))


class ProductDetail(ListView, FormView):
    template_name = 'product/product_detail.html'
    model = ProductModel
    context_object_name = "product"
    form_class = UserReviewForm

    def get_context_data(self, *, object_list=None, **kwargs):
        product = ProductModel.objects.get(id=self.kwargs.get('pk'))
        product.views = product.views + 1
        product.save()
        if self.request.user.is_authenticated:
            RecentlyViewedProducts.add_view(self.request.user, product)

        context = super(ProductDetail, self).get_context_data(**kwargs)
        active_discounts = DiscountPrice.objects.filter(is_active=True)
        context['active_discounts'] = ProductModel.objects.filter(discount__in=active_discounts)

        product_cat = product.category.all()
        context['same_category_product'] = ProductModel.objects.filter(category__in=product_cat).order_by(
            '-sell_count', '-views').distinct()[:8]

        return context

    def get_queryset(self, **kwargs):
        product = ProductModel.objects.get(id=self.kwargs.get('pk'))
        return product

    def form_valid(self, form, **kwargs):
        form = form.save(commit=False)
        form.product = get_object_or_404(ProductModel, id=self.kwargs.get('pk'))
        form.autor = self.request.user
        form.save()

        return redirect('product:Product_detail', pk=self.kwargs.get('pk'))
