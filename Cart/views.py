from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import ListView, View, FormView, CreateView
from Account.models import UserShippingAddress
from Product.models import ProductModel
from .cart_madule import Cart
from .models import Order, OrderedProduct, Coupon
from .forms import AddressForm
from django.contrib import messages
from django.utils import timezone
from django.db import transaction


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
        if int(quantity) < 1:
            messages.warning(request, "Not valid")

        else:
            cart = Cart(request)
            cart.add_to_cart(product, color, size, quantity)
            messages.success(request, "Product added to Cart")

        return redirect(request.META.get('HTTP_REFERER', '/'))


class DeleteItem(View):
    def get(self, request, pk):
        cart = Cart(request)
        cart.delete(pk)
        return redirect(request.META.get('HTTP_REFERER', '/'))


class CreateOrder(View):
    pass

    # def post(self, request):
    #     cart = Cart(self.request)
    #     address = request.POST.get('address')
    #     pay_method = request.POST.get('payment')
    #     if not address:
    #         class CreateAddress(CreateView):
    #             form_class = AddressForm
    #
    #             def form_valid(self, form):
    #                 form = form.save(commit=False)
    #                 form.user = self.request.user
    #                 form.save()
    #
    #         CreateAddress()
    #     shipping_address = UserShippingAddress.objects.get(id=address)
    #     order = Order.objects.create(user=self.request.user, total_price=cart.total(), address=shipping_address)
    #
    #     for item in cart:
    #         OrderedProduct.objects.create(order=order, product=item['product'], color=item['color'],
    #         size=item['size'],quantity=item['quantity'], price=item['price'])
    #
    #     if pay_method == "online":
    #         print('second')
    #         return
    #
    #     messages.success(self.request, "Order Places")
    #     return redirect('/')


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


@transaction.atomic
def apply_coupon(request):
    if request.method != 'POST':
        return redirect('cart:cart')

    if not request.user.is_authenticated:
        login_url = reverse('Account:login')
        referer = request.META.get('HTTP_REFERER', '/')
        return redirect(f'{login_url}?next={referer}')

    def raise_error(error_message="Invalid coupon!"):
        messages.error(request, str(error_message))
        return redirect('cart:cart')

    coupon_code = request.POST.get('coupon')
    date = timezone.now()

    coupon = Coupon.objects.filter(code=coupon_code, expiration__gte=date).first()
    if not coupon:
        return raise_error()

    if request.user in coupon.used_by.all():
        return raise_error("Coupon has already been used!")

    if coupon.limitation and coupon.limitation <= 0:
        return raise_error("Coupon usage limit exceeded!")

    cart_total = Cart(request).total()

    if coupon.discount_amount:
        total_price = max(cart_total - coupon.discount_amount, 0)
    else:
        total_price = max(cart_total - (cart_total * coupon.discount_percentage / 100), 0)

    coupon_session = request.session.get('coupon', [])
    coupon_session.append(total_price)
    request.session['coupon'] = coupon_session
    request.session.set_expiry(0)

    if coupon.limitation and coupon.limitation > 0:
        coupon.limitation -= 1

    coupon.used_by.add(request.user)
    coupon.save()

    messages.success(request, "Coupon applied successfully")
    return redirect('cart:cart')
