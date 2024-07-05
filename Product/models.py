import uuid
from django.db import models
from django.utils.text import slugify
from Account.models import User
from django.templatetags.static import static


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="subs")
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'


class Size(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'


class ProductModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="product name")
    product_description = models.TextField(null=True, blank=True, verbose_name="products short description ",
                                           help_text="located below the products name")
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.SmallIntegerField()
    available_amount = models.PositiveSmallIntegerField(verbose_name="available amount")
    color = models.ManyToManyField(Color, related_name="products", null=True, blank=True)
    size = models.ManyToManyField(Size, related_name="products", null=True, blank=True)

    category = models.ManyToManyField(Category, related_name="sub_products")

    short_point_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 1")
    short_point_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 2")
    short_point_3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 3")
    short_point_4 = models.CharField(max_length=100, null=True, blank=True, verbose_name="short point 4")
    information = models.TextField(null=True, blank=True)

    add_date = models.DateField(auto_now_add=True, verbose_name="added date", editable=False)
    last_update = models.DateField(auto_now=True, verbose_name="Last update", editable=False)

    favorites = models.ManyToManyField(User, related_name='favorites', editable=False)

    sell_count = models.PositiveSmallIntegerField(verbose_name="Sell mount", editable=False, default=0)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProductModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProductImages', null=True, blank=True)

    def __str__(self):
        return f'{self.product.title}`s Images'

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return static('static/img/no_product_image.png')

    # def save(self, *args, **kwargs):
    #     if not self.image:
    #         default_image_path = os.path.join(settings.STATIC_ROOT, 'img/no_product_image.png')
    #         with open(default_image_path, 'rb') as f:
    #             self.image.save('default_image.png', ContentFile(f.read()), save=False)
    #     super(ProductImage, self).save(*args, **kwargs)


class ProductComment(models.Model):
    Product = models.ForeignKey(ProductModel, related_name="comments", on_delete=models.CASCADE)
    autor = models.OneToOneField(User, related_name="comments", on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    email = models.EmailField()
    Review_text = models.TextField()
    spread_date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('spread_date',)
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return f'{self.Product.title}     ~     {self.spread_date}'


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


class DiscountPrice(models.Model):
    product = models.ForeignKey(ProductModel, related_name="discount", on_delete=models.CASCADE, null=True,
                                blank=True)  # => null and blank only for development purposes
    discount_rate = models.PositiveSmallIntegerField(verbose_name="discount in percentage", help_text="in percentage %")
    limit = models.PositiveSmallIntegerField(help_text="Code Limitation", null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.product.title} {self.discount_rate}% OFF '

    def reduced_price(self):
        return self.product.price - (self.product.price * self.discount_rate / 100)


class SiteTitleBanner(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="banner_image")
    product = models.ForeignKey(ProductModel, related_name="site_title", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
