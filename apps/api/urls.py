from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path("home", include("apps.home.urls", 'home')),
    path("user", include("apps.user.urls", 'user')),
    path("product", include("apps.product.urls", 'product')),
    path("carts", include("apps.carts.urls", 'carts')),
]
