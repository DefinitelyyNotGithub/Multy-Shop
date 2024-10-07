from django.shortcuts import get_object_or_404


def user_favorites_context(request):
    product_list: list = []

    if request.user.is_authenticated:
        from Account.models import User
        user = User.objects.get(id=request.user.id)
        product_list = user.favorites.all()

    else:
        try:
            from Product.models import ProductModel
            if request.session['favorites']:
                for id in request.session['favorites']:
                    product_list.append(ProductModel.objects.get(id=id))
        except:
            pass

    return {'favorites_': product_list, 'fav_len': len(product_list)}


def user_recent_viewed(request):
    if request.user.is_authenticated:
        from Product.models import RecentlyViewedProducts
        recently_viewed = RecentlyViewedProducts.objects.filter(user=request.user).order_by('-date').distinct()[:8]
        recent_viewed = [item.product for item in recently_viewed]
        return {"recent_viewed": recent_viewed}
    else:
        return ''


def site_general_info(request):
    from Home.models import SiteContact

    return {'site_general_info': SiteContact.objects.last(),
            'instagram_URL': SiteContact.objects.last().insta_account,
            'facebook_URL': SiteContact.objects.last().facebook,
            'linkin_URL': SiteContact.objects.last().linkin_account,
            'x_URL': SiteContact.objects.last().x_account,
            'Twitter_URL': SiteContact.objects.last().twitter_account,
            }


def cart(request):
    from Cart.cart_madule import Cart
    cart_ = Cart(request)
    cart_item: list = []
    from Product.models import ProductModel
    for item in cart_:
        product = get_object_or_404(ProductModel, id=item['product_id'])

        cart_item.append(
            product.id
        )

    return {'cart_len': len(cart_item), 'cart_includes': cart_item}
