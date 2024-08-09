from uuid import uuid4

from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False, verbose_name="MARK AS SEEN")

    def __str__(self):
        return f'{self.subject} --- {self.message[:20]}'

    class Meta:
        verbose_name = "User message"
        verbose_name_plural = "User messages"


class SiteContact(models.Model):
    site_description = models.TextField(null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    insta_account = models.URLField("Instagram URL", blank=True, max_length=255)
    linkin_account = models.URLField("Linkin URL", blank=True, max_length=255)
    facebook = models.URLField("Facebook URL", blank=True, max_length=255)
    x_account = models.URLField("X URL", blank=True, max_length=255)
    twitter_account = models.URLField("Tweeter URL", blank=True, max_length=255)

    def __str__(self):
        return f'contact information id:{self.id}'


class AboutUs_Model(models.Model):
    pottage = models.ImageField(upload_to='images/aboutus_title', null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    general_description = models.TextField(verbose_name="General description")

    def __str__(self):
        return self.general_description[:10]

    class Meta:
        verbose_name = "about us page"


class FAQs_model(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
