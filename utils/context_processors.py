from django.shortcuts import get_object_or_404


def user_favorites_context(request):
    favorite_list: list = []

    if request.user.is_authenticated:
        favorite_list.append(request.user.favorites.all())

    if 'favorites' in request.session:
        favorite = request.session['favorites']
        for fav in favorite:
            from Product.models import ProductModel
            product = get_object_or_404(ProductModel, id=fav)
            favorite_list.append(product)
    print(favorite_list)

    return {'favorites_': favorite_list, 'fav_len': len(favorite_list[0])}

