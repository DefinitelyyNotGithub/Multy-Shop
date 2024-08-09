from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('faq', views.FAQsView.as_view(), name="FAQs"),
    path('help', views.HelpView.as_view(), name="help"),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('about-us', views.AboutUsView.as_view(), name="About_us"),
    path('search', views.search, name="search"),
    path('newsteller', views.NewsLetterView.as_view(), name="news_letter"),
    path('', views.HomeView.as_view(), name="home"),

]
