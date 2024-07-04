from django.views.generic import ListView, TemplateView
from django.shortcuts import render, get_object_or_404
from .models import ProductModel, Category
from Account.models import User
from django.http import JsonResponse


# class ProductList(ListView):
#     template_name = 'product/product_list.html'
#     model = ProductModel

class NavBarView(TemplateView):
    template_name = 'includes/NavBar.html'

    def get_context_data(self, **kwargs):
        context = super(NavBarView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    paginate_by = 20
    context_object_name = 'obj'

    def get_queryset(self):
        pass


class CategoryProductList(ListView):
    template_name = 'product/product_list.html'
    model = ProductModel
    paginate_by = 33
    context_object_name = 'obj'

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
                queryset = queryset.filter(discount=True)
            elif sorted_by == 'all':
                queryset = queryset

            # if sorted_by == 'rating':
            #   queryset = queryset.order_by()

        return queryset


class UserFavoriteList(TemplateView):
    template_name = 'product/user_liked_products.html'


def add_to_favorites(request, pk):
    product = get_object_or_404(ProductModel, id=pk)
    user = request.user

    if request.user.is_authenticated:
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
    print(user.favorites.all())
    return JsonResponse({'status': 'successful'})
