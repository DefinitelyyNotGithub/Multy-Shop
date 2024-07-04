from django.urls import path
from .views import *

app_name = "product"

urlpatterns = [
    path('cat', NavBarView.as_view(), name="navbar"),
    path('category/<slug:cat>', CategoryProductList.as_view(), name="category_product_list"),
    path('shop', CategoryProductList.as_view(), name="product_list"),
    path('favorite', UserFavoriteList.as_view(), name="user_favorite_list"),
    path('add_favorite/<int:pk>', add_to_favorites, name="add_to_user_favorite_list"),

]
