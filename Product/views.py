from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from .models import ProductModel, Category


# class ProductList(ListView):
#     template_name = 'product/product_list.html'
#     model = ProductModel

class NavBarView(TemplateView):
    template_name = 'includes/NavBar.html'

    def get_context_data(self, **kwargs):
        context = super(NavBarView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
