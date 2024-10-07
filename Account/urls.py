from django.urls import path
from . import views

app_name = "Account"

urlpatterns = [
    path('login', views.UserLogInView.as_view(), name="login"),
    path('logout', views.Logout, name="logout"),
    path('register', views.Register.as_view(), name="register"),
    path('ValidationCode', views.CodeValidation.as_view(), name="code validation"),
    path('user/profile/add-shipping-adress', views.AddShippingAddress.as_view(), name="profile_add_shipping-address"),
    path('user/profile', views.UserProfile.as_view(), name="user_profile"),

]
