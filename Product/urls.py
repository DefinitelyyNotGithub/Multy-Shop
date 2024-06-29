from django.urls import path
from .views import *

app_name = "product"

urlpatterns = [
    path('category', NavBarView.as_view(), name="navbar"),

]
