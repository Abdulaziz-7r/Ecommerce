"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from phone import views as phv
from phone_api import views as p_api
from furniture import views as frv

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", phv.index, name="home"),
    path("showphone/", phv.show_phone, name="show_phone"),
    path("details/<int:id>/", phv.details, name="details"),
    path("auth_login/", phv.auth_login, name="auth_login"),
    path("auth_register/", phv.auth_register, name="auth_register"),
    path("auth_logout/", phv.auth_logout, name="auth_logout"),
    path("checkout/", phv.checkout, name="checkout"),
    path("cart/", phv.cart, name="cart"),
    path("add_to_cart/<int:product_id>/", phv.add_to_cart, name="add_to_cart"),
    path("buy_now/<int:product_id>/", phv.buy_now, name="buy_now"),
    path("api/itemlist/all/", p_api.get_all_items_list, name="get_all_items_list"),
    path(
        "api/itemdetailslist/all/",
        p_api.get_all_items_details_list,
        name="get_all_items_details_list",
    ),
    path(
        "api/get_all_items_details_by_id/<int:id>/",
        p_api.get_all_items_details_by_id,
        name="get_all_items_details_by_id",
    ),
    path("show_furniture/", frv.show_furniture, name="show_furniture"),
    path(
        "furniture_details/<int:id>/", frv.furniture_details, name="furniture_details"
    ),
    path(
        "add_to_cart_furniture/<int:product_id>/",
        frv.add_to_cart_furniture,
        name="add_to_cart_furniture",
    ),
    path(
        "buy_now_furniture/<int:product_id>/",
        frv.buy_now_furniture,
        name="buy_now_furniture",
    ),
    path("checkout_furniture/", frv.checkout_furniture, name="checkout_furniture"),
    path("delete_item_phone/<int:id>/", phv.delete_item_phone, name="delete_item_phone"),
]
