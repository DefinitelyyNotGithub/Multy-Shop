from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart', views.CartView.as_view(), name="cart"),
    path('add-cart/<int:pk>', views.AddToCart.as_view(), name="add_to_cart"),
    path('cart/delete/<str:pk>', views.DeleteItem.as_view(), name="Delete_cart"),
    path('add_checkout', views.CheckOut.as_view(), name="check_out"),
    path('checkout', views.CreateOrder.as_view(), name="place_order"),
    path('aplay/coupon', views.apply_coupon, name="apply_coupon"),


]