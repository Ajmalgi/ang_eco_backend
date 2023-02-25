from django.urls import path
from . import views

urlpatterns = [
    
    path('addproduct',views.addproduct),
    path('change_password/<int:id>',views.change_pswd),
    path('Sview_products',views.Sview_products),
    path('update_stock',views.update_stock),
  
  
]