"""OnlineShopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from shopping_app import views

urlpatterns = [
    url(
        r'^$',
        views.signin,
        name='index'
    ),
    url(
        r"^signup$",
        views.signup,
        name="signup"
    ),
    url(
        r"^signin$",
        views.signin,
        name="signin"
    ),
    url(
        r"^homepage$",
        views.homepage,
        name="homepage"
    ),
    url(
        r"^cart$",
        views.view_cart,
        name="cart"
    ),
    url(
        r"^add_product$",
        views.add_product,
        name="add_product"
    ),
    url(
        r"^logout$",
        views.logout,
        name="logout"
    ),
    url(
        r'^new_arrival/$',
        views.new_arrival,
        name='new_arrival'
    ),
    url(
        r'^by_discount/$',
        views.sort_by_discount,
        name='by_discount'
    ),
    url(
        r'^high_to_low/$',
        views.sort_high_to_low,
        name='high_to_low'
    ),
    url(
        r'^low_to_high/$',
        views.sort_low_to_high,
        name='low_to_high'
    ),
    url(
        r"^add_to_cart/(?P<item_name>[\w \d]+)$",
        views.add_to_cart,
        name="add_to_cart"
    ),
    url(
        r"^remove_item/(?P<item_id>[0-9]+)$",
        views.remove_item,
        name="remove_item"
    )
]
