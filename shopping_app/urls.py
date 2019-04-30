"""OnlineShopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from shopping_app import views

urlpatterns = [
    path(
        '',
        views.signin,
        name='index'
    ),
    path(
        "signup",
        views.signup,
        name="signup"
    ),
    path(
        "signin",
        views.signin,
        name="signin"
    ),
    path(
        "homepage",
        views.homepage,
        name="homepage"
    ),
    path(
        "cart",
        views.view_cart,
        name="cart"
    ),
    path(
        "add_product",
        views.add_product,
        name="add_product"
    ),
    path(
        "logout/",
        views.logout,
        name="logout"
    ),
    path(
        r"remove_item/(?P<item_id>[0-9]+)",
        views.remove_item,
        name="remove_item"
    )
]
