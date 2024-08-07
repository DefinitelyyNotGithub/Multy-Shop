from django.db import models


# class Order(models.Model):
#     user = models.ForeignKey('User', related_name='order', on_delete=models.CASCADE)
#     address = models.ForeignKey('UserShippingAddress', related_name='order', on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     total_price = models.PositiveSmallIntegerField(editable=False)
#     is_paid = models.BooleanField(default=False)
#     delivered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f' {self.address.first_name} {self.address.last_name} -- {self.date}'


# class OrderedProduct(models.Model):
#     # order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="instance")
#     price = models.IntegerField(default=0)
#     product = models.ForeignKey('ProductModel', on_delete=models.CASCADE, related_name="product")
#     size = models.CharField(max_length=100, null=True, blank=True)
#     color = models.CharField(max_length=100, null=True, blank=True)
#     quantity = models.SmallIntegerField()
#
#     def __str__(self):
#         return self.product.title
#
#     class Meta:
#         verbose_name = "order"
#         verbose_name_plural = "orders"
