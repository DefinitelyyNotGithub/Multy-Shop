from django.db import models
from django.utils.text import slugify
from django.templatetags.static import static
from django.urls import reverse


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="subs")
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='img/category_images', null=True, blank=True)
    on_first_page = models.BooleanField(default=False, verbose_name="main page categories",
                                        help_text="be shown on first page category")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    def category_image(self):
        if self.image:
            return self.image.url
        else:
            return static('img/no_product_image.png')

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.title}'


class Size(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.title}'


class ProductModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="product name")
    product_description = models.TextField(null=True, blank=True, verbose_name="products short description ",
                                           help_text="located below the products name")
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.FloatField()
    available_amount = models.PositiveSmallIntegerField(verbose_name="available amount")
    color = models.ManyToManyField(Color, related_name="products", blank=True)
    size = models.ManyToManyField(Size, related_name="products", blank=True)

    category = models.ManyToManyField(Category, related_name="sub_products", blank=True)

    short_point_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 1")
    short_point_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 2")
    short_point_3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 3")
    short_point_4 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 4")
    information = models.TextField(null=True, blank=True)

    add_date = models.DateField(auto_now_add=True, verbose_name="added date", editable=False)
    last_update = models.DateField(auto_now=True, verbose_name="Last update", editable=False)

    # favorites = models.ManyToManyField(User, related_name='favorites', editable=False)

    sell_count = models.PositiveSmallIntegerField(verbose_name="Sell mount", editable=False, default=0)
    views = models.PositiveIntegerField(default=0, editable=False)

    def product_image(self):
        if self.images.all():
            return self.images.first().image.url
        else:
            return static('img/no_product_image.png')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(ProductModel, self).save(*args, **kwargs)

    def get_absolute_data(self):
        return reverse('product:Product_detail', args=[self.id])

    def product_price(self):
        try:
            global_offer = DiscountPrice.objects.filter(apply_to_all_products=True, is_active=True).last()
            product_price = self.price - (self.price * global_offer.discount_rate / 100)
            print(product_price)
            return product_price
        except:
            try:
                discount = DiscountPrice.objects.get(product=self, is_active=True)
                product_price = self.price - (self.price * discount.discount_rate / 100)

                return product_price
            except:
                product_price = self.price
                return product_price

    def __str__(self):
        return f'{self.title}'


class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/ProductImages', null=True, blank=True)

    def __str__(self):
        return f'{self.product.title}`s Images'


class ProductComment(models.Model):
    product = models.ForeignKey(ProductModel, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    Review_text = models.TextField()
    spread_date = models.DateField(auto_now_add=True, editable=False)
    autor = models.ForeignKey('Account.User', related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-spread_date',)
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return f'{self.product.title}  ~  {self.spread_date}'


class ProductEAV(models.Model):
    product = models.ForeignKey(ProductModel, related_name="product_EAV", on_delete=models.CASCADE)
    color = models.ForeignKey(Color, related_name="color_EAV", on_delete=models.CASCADE)
    size = models.ForeignKey(Size, related_name="size_EAV", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.product.title}-----({self.quantity})-----{self.color.title} '

    class Meta:
        verbose_name = "product color and size"
        ordering = ['-quantity']


class RecentlyViewedProducts(models.Model):
    product = models.ForeignKey(ProductModel, related_name="recent_viewed", on_delete=models.CASCADE)
    user = models.ForeignKey('Account.User', related_name="recent_viewed", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def add_view(cls, user, product):
        recent_views = cls.objects.filter(user=user).order_by('-date')

        if recent_views.filter(product=product).exists():
            cls.objects.filter(product=product).delete()

        cls.objects.create(user=user, product=product)
        cls.cleanup_old_entries(user=user)

    @classmethod
    def cleanup_old_entries(cls, user):
        recent_views = cls.objects.filter(user=user).order_by('-date')

        if recent_views.count() > 20:
            ids_to_delete = recent_views.values_list('id', flat=True)[20:]
            cls.objects.filter(id__in=ids_to_delete).delete()

    def __str__(self):
        return f'{self.product.title} -- {self.date}'


class DiscountPrice(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="event name")
    product = models.ManyToManyField(ProductModel, related_name='discount')
    discount_rate = models.PositiveSmallIntegerField(verbose_name="discount in percentage", help_text="in percentage %",
                                                     default=0)
    limit = models.PositiveSmallIntegerField(help_text="limitation", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="is active")
    apply_to_all_products = models.BooleanField(default=False, verbose_name="Apply discount for all products")

    def __str__(self):
        return f'{self.name} --- {self.discount_rate}% OFF '


class SiteTitleBanner(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="img/banner_image")
    product = models.ForeignKey(ProductModel, related_name="site_title", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
