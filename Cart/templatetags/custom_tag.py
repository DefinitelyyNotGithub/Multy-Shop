from django import template

register = template.Library()


@register.filter(name="shipping_price")
def shipping_price(value):
    return int(value) + int(10)
