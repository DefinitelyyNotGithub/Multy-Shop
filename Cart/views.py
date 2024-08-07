from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, View

from Product.models import ProductModel
from .cart_madule import Cart


class CartView(ListView):
    template_name = 'cart/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        cart = Cart(self.request)
        return cart


class AddToCart(View):
    def post(self, request, pk):
        product = get_object_or_404(ProductModel, id=pk)
        color, size, quantity = request.POST.get('color'), request.POST.get('size'), request.POST.get('quantity')
        cart = Cart(request)
        cart.add_to_cart(product, color, size, quantity)
        return redirect(request.META.get('HTTP_REFERER', '/'))


class DeleteItem(View):
    def get(self, request, pk):
        print(pk)
        cart = Cart(request)
        cart.delete(pk)
        return redirect(request.META.get('HTTP_REFERER', '/'))
