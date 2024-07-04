from Product.models import ProductModel, DiscountPrice
from django import template

register = template.Library()


@register.filter(name="price")
def discount(value):
    try:
        obj = ProductModel.objects.get(id=value.id)
        discount = DiscountPrice.objects.get(product=obj)
        discounted_price = obj.price - (obj.price * discount.discount_rate / 100)
        return discounted_price
    except (ProductModel.DoesNotExist, DiscountPrice.DoesNotExist):
        return value.price
