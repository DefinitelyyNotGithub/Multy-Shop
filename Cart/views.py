from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, View, FormView
from Account.models import UserShippingAddress
from Product.models import ProductModel
from .cart_madule import Cart
# from .models import Order, OrderedProduct
from . forms import AddressForm


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


# class CreateOrder(View):
#     def get(self, request):
#         cart = Cart(request)
#
#         order = Order.objects.create(user=request.user, address=UserShippingAddress, total_price=cart.total())
#         for item in cart:
#             OrderedProduct.objects.create(order=order, product=item['product'], color=item['color'], size=item['size']
#                                           , quantity=item['quantity'], price=item['price'])
#
#         return redirect(request.META.get('HTTP_REFERER', '/'))

class CheckOut(ListView, FormView):
    template_name = 'cart/checkout.html'
    context_object_name = 'cart'
    form_class = AddressForm

    def get_queryset(self):
        cart = Cart(self.request)
        return cart

    def form_valid(self, form):
        form.save()

