# from django.templatetags.static import static
# from Product.models import ProductModel, DiscountPrice
# from django import template
# from django.shortcuts import get_object_or_404
#
# register = template.Library()
#
#
# @register.filter(name="price")
# def discount(value):
#     product = get_object_or_404(ProductModel, id=value.id)
#     try:
#         global_offer = DiscountPrice.objects.filter(apply_to_all_products=True, is_active=True).last()
#         product_price = product.price - (product.price * global_offer.discount_rate / 100)
#         return product_price
#     except:
#         try:
#             discount = DiscountPrice.objects.get(product=product, is_active=True)
#             product_price = product.price - (product.price * discount.discount_rate / 100)
#             return product_price
#         except:
#             product_price = product.price
#             return product_price
