from Product.models import ProductModel, DiscountPrice


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            product = ProductModel.objects.get(id=int(item['product_id']))
            item['product'] = product
            item['total'] = int(product.product_price()) * int(item['quantity'])
            item['uid'] = self.unique_id_generator(product, item['color'], item['size'])
            yield item

    def unique_id_generator(self, product, color, size):
        uid = f'{product.id}-{color}-{size}'
        return uid

    def add_to_cart(self, product, color, size, quantity):
        unique_id = self.unique_id_generator(product, color, size)
        if unique_id not in self.cart:
            self.cart[unique_id] = {'product_id': product.id, 'color': color, 'size': size, 'quantity': 0,
                                    'price': str(product.price)}
        self.cart[unique_id]['quantity'] += int(quantity)
        self.save()

    def delete(self, uid):
        if uid in self.cart:
            del self.cart[uid]
            self.save()

    def total(self):
        return sum(float(item['price']) * int(item['quantity']) for item in self.cart.values())



    def save(self):
        self.session.modified = True
