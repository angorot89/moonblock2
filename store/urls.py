from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('skip-auth/', views.skip_auth_view, name='skip_auth'),
    path('logout/', views.logout_view, name='logout'),
    path('shop/', views.shop, name='shop'),
    path('sizing-guide/', views.sizing_guide, name='sizing_guide'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('lookbook/', views.lookbook, name='lookbook'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
    path('api/cart/update/', views.update_cart, name='update_cart'),
    path('api/cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('lang/<str:lang>/', views.set_language, name='set_language'),
    path('audience/<str:audience>/', views.set_audience, name='set_audience'),
]
