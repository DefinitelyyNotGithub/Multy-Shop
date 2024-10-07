from django.db import models, transaction
from Account.models import UserShippingAddress, User
from Product.models import ProductModel
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    address = models.ForeignKey(UserShippingAddress, related_name='order', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveSmallIntegerField(editable=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.address.first_name} {self.address.last_name} -- {self.date}'


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="instance")
    price = models.IntegerField(default=0)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product")
    size = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "ordered product"
        verbose_name_plural = "ordered products"


class Coupon(models.Model):
    code = models.CharField(unique=True, max_length=100, null=True, blank=True,
                            help_text="will be filled automatically if not entered ")
    used_by = models.ManyToManyField(User, blank=True, related_name="used_coupons", editable=False)
    discount_percentage = models.PositiveSmallIntegerField(default=0, verbose_name="discount percentage", null=True
                                                           , blank=True)
    discount_amount = models.PositiveSmallIntegerField(default=0, verbose_name="decrement amount", null=True, blank=True)
    limitation = models.PositiveSmallIntegerField(null=True, blank=True)
    expiration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f' {self.code} --- {self.discount_percentage}'

    def clean(self):
        if self.discount_percentage and self.discount_amount:
            raise ValidationError("cant use discount_percentage and discount_mount together ")
        super(Coupon, self).clean()

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.code:
            while True:
                random_code = get_random_string(length=8)
                if not Coupon.objects.filter(code=random_code).exists():
                    self.code = random_code
                    break

        return super(Coupon, self).save(*args, **kwargs)
