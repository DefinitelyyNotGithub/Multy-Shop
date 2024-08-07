from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone=phone,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    phone = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=45)
    from Product.models import ProductModel
    favorites = models.ManyToManyField(ProductModel, related_name="favorites", null=True, blank=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone"  # => it used to be email
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class RegisterModel(models.Model):
    phone = models.CharField(max_length=11, verbose_name="Phone Number")
    password = models.CharField(max_length=16)
    token = models.UUIDField(unique=True)
    random_code = models.SmallIntegerField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'( {self.phone} )'

    class Meta:
        ordering = (
            'created',
        )
        verbose_name = " unauthenticated user"
        verbose_name_plural = " unauthenticated users"


class UserExtraInfo(models.Model):
    user = models.ForeignKey(User, related_name="extra_info", on_delete=models.CASCADE)
    receiver = models.CharField(max_length=100, verbose_name="receiver name ")
    phone = models.CharField(max_length=12)
    address = models.TextField()
    post_code = models.CharField(max_length=40)

    def __str__(self):
        return self.user.full_name if self.user.full_name else self.receiver
