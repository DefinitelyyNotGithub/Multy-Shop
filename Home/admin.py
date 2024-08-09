from django.contrib import admin
from .models import (
    Contact,
    FAQs_model,
    NewsLetter,
    SiteContact,
    AboutUs_Model,
)


@admin.register(Contact)
class ContactAdminModel(admin.ModelAdmin):
    list_filter = ['seen', ]


admin.site.register(SiteContact)
admin.site.register(AboutUs_Model)
admin.site.register(FAQs_model)
admin.site.register(NewsLetter)
