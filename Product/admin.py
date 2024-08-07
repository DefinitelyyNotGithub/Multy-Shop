from django.contrib import admin

from .models import (

    Size,
    Color,
    Category,
    ProductEAV,
    ProductImage,
    ProductModel,
    DiscountPrice,
    ProductComment,
    SiteTitleBanner,
    RecentlyViewedProducts,
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    search_help_text = "search the category"
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'available_amount', 'price', 'views']
    list_filter = ['available_amount', 'add_date', 'last_update']
    inlines = [ProductImageInline, ]
    search_fields = ['title', ]
    search_help_text = "Search the product`s name"
    autocomplete_fields = ['category']
    list_per_page = 25


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_filter = ['spread_date', ]


@admin.register(DiscountPrice)
class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_rate']
    search_fields = ['discount_rate', 'name']
    autocomplete_fields = ['product']
    filter_horizontal = ['product']


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductEAV)
admin.site.register(SiteTitleBanner)
admin.site.register(RecentlyViewedProducts)
