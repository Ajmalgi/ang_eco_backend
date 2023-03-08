
from django.urls import path
from . import views

urlpatterns = [
    
    path('seller_reg',views.seller_reg),
    path('seller_login',views.seller_login),
    path('customer_reg',views.customer_reg),
    path('customer_login',views.customer_login),
    path('view_products',views.view_products),
    path('customer_profile',views.customer_profile),
    path('home_category',views.home_category),
    path('product_details/<int:id>',views.product_details),
    path('addto_cart',views.addto_cart),
    path('my_cart',views.my_cart),
    path('s_email_check',views.s_email_check),
    path('remove_cart_item',views.remove_cart_item),
]