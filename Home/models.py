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
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    address = models.TextField()

    insta_account = models.CharField(max_length=100)
    linkin_account = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    x_account = models.CharField(max_length=100)

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
